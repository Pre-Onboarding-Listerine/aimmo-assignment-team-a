from django.db import models
from django.db.models.deletion import CASCADE
from core.models import TimeStampModel


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'categories'


class Posting(TimeStampModel):
    post_id = models.AutoField(primary_key=True, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.TextField()
    author = models.CharField(max_length=64)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    view_count = models.IntegerField()
    user_ids = models.TextField()

    class Meta:
        db_table = 'postings'


class Comment(TimeStampModel):
    comment_id = models.AutoField(primary_key=True, null=False)
    author = models.CharField(max_length=64)
    content = models.TextField()
    post = models.ForeignKey('Posting', on_delete=models.CASCADE)
    depth = models.BooleanField()
    bundle_id = models.IntegerField()
    bundle_order = models.DateTimeField()

    class Meta:
        db_table = 'comments'
