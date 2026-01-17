from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = Post.objects.filter(author=request.user)
