from django.shortcuts import render
from .models import Post 
from .serializers import PostSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


    