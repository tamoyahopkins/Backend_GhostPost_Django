from rest_framework import viewsets
# from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import action

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def vote(self, u_id, vote_type):
        post = Post.objects.get(u_id=u_id)
        if vote_type == 'up':
            post.up += 1
            post.save()
        else:
            post.down += 1
            post.save()


    def delete_post(self, u_id):
        post = Post.objects.get(u_id=u_id)
        post.delete()
