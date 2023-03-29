from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogpostSerializer

@api_view(['GET', 'POST'])
def blogpost_list(request):
    if request.method == 'GET':
        blogposts = BlogPost.objects.all()
        serializer = BlogpostSerializer(blogposts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BlogpostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def blogpost_detail(request, pk):
    try:
        blogpost = BlogPost.objects.get(id=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogpostSerializer(blogpost)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BlogpostSerializer(blogpost, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
