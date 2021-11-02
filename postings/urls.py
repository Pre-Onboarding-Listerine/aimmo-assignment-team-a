from django.urls import path
from postings.views import PostingsListView, PostingView, PostingDetailView


urlpatterns = [
    path('', PostingsListView.as_view()),
    path('/posting', PostingView.as_view()),
    path('/posting/<int:post_id>', PostingDetailView.as_view())
]
