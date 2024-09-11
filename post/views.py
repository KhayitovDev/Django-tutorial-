
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


from .models import Post 
from .serializers import PostSerializer


@api_view(['POST', 'GET'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serialzier = PostSerializer(posts, many=True)
        return Response(serialzier.data)
    elif request.method == "POST":
        serialzier = PostSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=201)
        return Response(serialzier.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=404)
    
    if request.method == "GET":
        serialzier = PostSerializer(post)
        return Response(serialzier.data)
    elif request.method == "PUT":
        serialzier = PostSerializer(post, data=request.data, partial = True)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data)
        return Response(serialzier.errors, status=400)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=204)
    
class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

        
        

        

    




   



    
