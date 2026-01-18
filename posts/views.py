from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListCreateView(ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(pk=self.request.post.pk)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user, post=self.request.post)
