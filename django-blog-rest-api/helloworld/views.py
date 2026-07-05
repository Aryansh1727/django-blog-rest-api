from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import PostFilter

class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filterset_class = PostFilter
    search_fields = ['title', 'content']
    ordering_fields = ['id']

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        