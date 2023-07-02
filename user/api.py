from user.models import Users
from rest_framework import viewsets, permissions
from .serializers import UsersSerializer

# Lead Viewset
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]