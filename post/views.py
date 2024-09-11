
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


from .models import Post 
from .serializers import PostSerializer


    