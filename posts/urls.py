from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="posts-list-create"),
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<slug:post_slug>/comments/",
        CommentListCreateView.as_view(),
        name="post-comments",
    ),
]
