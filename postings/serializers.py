from rest_framework import serializers
from postings.models import Category, Posting, Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category_id',
                  'name')


class PostingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posting
        fields = ('post_id',
                  'category',
                  'title',
                  'content',
                  'author',
                  'user',
                  'view_count')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posting
        fields = ('comment_id',
                  'author',
                  'content',
                  'post_id',
                  'depth',
                  'bundle_id',
                  'bundle_order')
