import json
from django.db.models import Q

from django.views.generic.base import View
from django.http.response import JsonResponse
from core.utils import authentication

from postings.models import Posting, Comment, Category
from users.models import User


class PostingsListView(View):
    def get(self, request):
        try:
            offset = int(request.GET.get("offset", 0))
            limit = int(request.GET.get("limit", 7))
            ordering = request.GET.get("ordering", "created_at")
            search_keyword = request.GET.get("keyword", None)
            q = Q()
            if search_keyword:
                q &= Q(title__icontains=search_keyword)
            posts_query = Posting.objects.all().order_by(ordering)
            posts = posts_query[offset : offset + limit]
            posts_count = posts_query.count()

            result = {"count": posts_count, "data": []}

            for post in posts:
                result["data"].append(
                    {
                        "author": post.user.name,
                        "title": post.title,
                        "content": post.content,
                        "created_at": post.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                    }
                )

            return JsonResponse({"results": result}, status=200)

        except KeyError:
            return JsonResponse({"MESSAGE": "Page Does Not Exists"}, status=404)
        except ValueError:
            return JsonResponse({"MESSAGE": "Write Integer, Not String"}, status=400)


class PostingDetailView(View):
    def get(self, request, posting_id):
        try:
            offset = int(request.GET.get("offset", 0))
            limit = int(request.GET.get("limit", 7))
            ordering = request.GET.get("ordering", "created_at")

            if not Posting.objects.filter(posting_id=posting_id).exists():
                return JsonResponse({"MESSAGE": "Does Not exist Posting"}, status=404)
            post = Posting.objects.get(posting_id=posting_id)
            comment_query = Comment.objects.filter(posting_id=posting_id).order_by(
                ordering
            )
            comments = comment_query[offset : offset + limit]
            comment_count = comment_query.count()

            result = {
                "author": post.author,
                "title": post.title,
                "content": post.content,
                "created_at": post.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "commnent_count": comment_count,
                "comments": [],
            }

            for comment in comments:
                result["data"].append(
                    {
                        "comment_id": comment.comment_id,
                        "author": comment.author,
                        "content": comment.content,
                        "depth": comment.depth,
                        "bundle_id": comment.bundle_id,
                        "bundle_order": comment.bundle_order,
                    }
                )

            return JsonResponse({"RESULT": result}, status=200)
        except KeyError:
            return JsonResponse({"MESSAGE": "Page Does Not Exists"}, status=404)
        except ValueError:
            return JsonResponse({"MESSAGE": "Write Integer, Not String"}, status=400)


class PostingView(View):
    @authentication
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = request.user
            title = data["title"]
            content = data["content"]
            category = data["category"]
            category = Category.objects.create(name=category)
            # 중복 조회수는 세지않도록
            # view_count =
            post = Posting.objects.create(
                category_id=category.category_id,
                title=title,
                content=content,
                author=user.name,
                user=user
                # view_count=
                # users_ids=
            )

            result = {
                "author": post.author,
                "title": post.title,
                "content": post.content,
                "created_at": post.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
            }

            return JsonResponse(
                {"MESSAGE": "Posting Success", "RESULT": result}, status=200
            )

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

    @authentication
    def put(self, request):
        try:
            data = json.loads(request.body)
            post_id = data["post_id"]
            title = data["title"]
            content = data["content"]

            if not Posting.objects.filter(id=post_id).exists():
                return JsonResponse({"MESSAGE": "DOSE_NOT_EXIST_POST"}, status=404)
            if Posting.objects.get(id=post_id).user.id != request.user.id:
                return JsonResponse({"MESSAGE": "NO_PERMISSION"}, status=401)

            Posting.objects.filter(id=post_id).update(title=title, content=content)

            return JsonResponse({"MESSAGE": "EDIT SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"MESSAGE": "VALUE_ERROR"}, status=400)

    @authentication
    def delete(self, request):
        try:
            data = json.loads(request.body)
            post_id = data["post_id"]

            if not Posting.objects.filter(id=post_id).exists():
                return JsonResponse(
                    {"MESSAGE": "Does Not Choose Correct Posting_ID"}, status=404
                )
            if Posting.objects.get(id=post_id).user.id != request.user.id:
                return JsonResponse({"MESSAGE": "NO_PERMISSION"}, status=401)

            Posting.objects.filter(id=post_id).delete()

            return JsonResponse({"MESSAGE": f"SUCCESS DELETE POST_ID : {post_id}"})

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
        except ValueError:
            return JsonResponse({"MESSAGE": "VALUE_ERROR"}, status=400)


class CommentView(View):
    @authentication
    def post(self, request, **kwargs):
        try:
            posting = Posting.objects.get(posting_id=kwargs["posting_id"])
            print(posting)
            user = request.user
            data = json.loads(request.body)
            print(data)
            print(user)
            author = user.name
            print(author)
            content = data["content"]
            print(content)
            depth = int(data["depth"])
            print(depth)
            # 0 이면 원댓글, 1이면 대댓글
            # if not depth == 0 or 1:
            #     return JsonResponse({"MESSAGE": "depth must be Boolean"})

            bundle_id = int(data["bundle_id"])

            comment = Comment.objects.create(
                author=author,
                content=content,
                posting_id=posting.posting_id,
                depth=depth,
                bundle_id=bundle_id,
            )

            print(comment)
            result = {
                "author": comment.author,
                "content": comment.content,
                "posting_id": comment.posting_id,
                "depth": comment.depth,
                "bundle_id": comment.bundle_id,
            }

            return JsonResponse(
                {"MESSAGE": "Posting Success", "RESULT": result}, status=200
            )

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
