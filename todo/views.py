from rest_framework import viewsets, permissions
from .models import Todo, Comment
from .serializers import TodoSerializer, CommentSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Todo.objects.all()
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)