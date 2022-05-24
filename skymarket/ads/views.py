from rest_framework import pagination, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer, CommentCreateSerializer, AdListSerializer, AdCreateSerializer
from ads.permissions import IsOwner

from ads.filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdMeModelView(viewsets.ModelViewSet):
    
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    permission_classes = [IsOwner]
    serializer_class = AdListSerializer
    
    def get_queryset(self):
        return Ad.objects.filter(author__exact=self.request.user)




class AdModelView(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    
    def get_permissions(self):
        permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
        
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        if self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]
        
        
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AdListSerializer
        if self.action == 'retrieve':
            return AdDetailSerializer
        if self.action == 'create':
            return AdCreateSerializer
        if self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            return AdDetailSerializer
        return AdSerializer
        
    def create(self, request, *args, **kwargs):
        new_ad = request.data
        new_ad['author'] = request.user.pk
        print(new_ad)
        
        serializer = self.get_serializer(data=new_ad)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
    

class CommentModelView(viewsets.ModelViewSet):
    pagination_class = AdPagination
    
        
    def get_queryset(self):
        return Comment.objects.filter(ad_id__exact=self.kwargs['aid'])
    
    def get_permissions(self):
        permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        if self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]
        
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CommentSerializer
        if self.action == 'retrieve':
            return CommentSerializer
        if self.action == 'create':
            return CommentCreateSerializer
        if self.action == 'destroy' or self.action == 'update' or self.action == 'partial_update':
            return CommentCreateSerializer
        return CommentSerializer
        
        
    def create(self, request, *args, **kwargs):
        new_comment = request.data
        new_comment['ad'] = self.kwargs['aid']
        new_comment['author'] = request.user.id
        
        serializer = self.get_serializer(data=new_comment)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
