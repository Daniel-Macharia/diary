from rest_framework import generics

from userAuth.models import User
from memory.models import Event as Memory

from .serializers import UserSerializer, MemorySerializer


# Create your views here.
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpecificUserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MemoryAPIView(generics.ListAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

class SpecificMemoryAPIView(generics.RetrieveAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

