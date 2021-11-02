from django.urls import path
from postings.views import PostingsListView, PostingView, PostingDetailView, CommentView


urlpatterns = [
    path("", PostingsListView.as_view()),
    path("/posting", PostingView.as_view()),
    path("/posting/<int:posting_id>", PostingDetailView.as_view()),
    path("/posting/<int:posting_id>/comment", CommentView.as_view()),
]
