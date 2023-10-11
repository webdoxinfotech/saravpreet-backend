from django.shortcuts import render
from rest_framework import viewsets,permissions
from api.serializers import PostSerializer
from api.models import Post
from rest_framework import filters
from rest_framework import generics
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class SearchAPIView(generics.ListCreateAPIView):
    search_fields = ['title', 'text']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer