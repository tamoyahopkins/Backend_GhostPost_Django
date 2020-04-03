from rest_framework import viewsets
from django.shortcuts import get_object_or_404, render, redirect
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse, HttpRequest


'''
NOTES
    CREATE POST
        curl -d '{"post_type":"B", "text":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:8001/api/post/
    VOTE ON POST 
        curl -X POST http://localhost:8001/api/post/{post.id}/vote_{up or down}/
    DELETE (REGULR)
        curl -X DELETE http://localhost:8001/api/post/3/
    CUSTOM DELETE (BY UNIQUE STRING)
        http://localhost:8001/api/post/797493/custom_delete
    ADD UNIQUE QUERY PARAMS TO REQUEST
        curl -X DELETE "http://localhost:8001/api/post/7/custom_delete/?a=foo"
        ADDS request.query_params --> QUERY PARAMS <QueryDict: {'a': ['foo']}>
'''


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    @action(detail=True, methods=['POST'])
    def vote_up(self, request, *args, **kwargs):
        '''request example: curl -X POST http://localhost:8001/api/post/{post.id}/vote_up/'''
        instance = self.get_object()
        instance.up += 1
        instance.save()
        return Response({'status': 'vote-up updated successfully'})


    @action(detail=True, methods=['POST'])
    def vote_down(self, request, *args, **kwargs):
        '''request example: curl -X POST http://localhost:8001/api/post/{post.id}/vote_down/'''
        instance = self.get_object()
        instance.down += 1
        instance.save()
        return Response({'status': 'vote-down updated successfully'})


    @action(detail=True, methods=['DELETE', 'GET'])
    def custom_delete(self, request,*args, **kwargs):
        '''request example: http://localhost:8001/api/post/797493/custom_delete'''
        # print('ARGS', args, 'KWARGS', kwargs)
        # print('QUERY PARAMS', request.query_params)
        item = Post.objects.filter(u_id=kwargs['pk'])
        item.delete()
        return Response({'status': f'Successfully deleted object u_id: {kwargs["pk"]}.'})
