from django.urls import path
from postings.views import PostingsListView ,PostingView,PostingEditView,PostingDeleteView


urlpatterns = [
    path('', PostingsListView.as_view()),
    path('/post', PostingView.as_view()),
    path('/edit', PostingEditView.as_view()),
    path('/delete',PostingDeleteView.as_view())
]