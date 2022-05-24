from rest_framework import serializers

from ads.models import Ad, Comment
from users.serializers import UserForAdSerialiser


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
class AdForCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title']


class CommentCreateSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.CharField(source='author.image', read_only=True)
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    
    
    class Meta:
        model = Comment
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_image = serializers.CharField(source='author.image')
    author_id = serializers.IntegerField(source='author.id')
    ad_id = serializers.IntegerField(source='ad.id')
    
    class Meta:
        model = Comment
        fields = ['pk', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id', 'author_image']



class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdCreateSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    
    class Meta:
        model = Ad
        exclude = ['created_at', 'author']



class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    phone = serializers.CharField(source='author.phone')
    author_id = serializers.IntegerField(source='author.id')
    
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description', 'phone', 'author_first_name', 'author_last_name', 'author_id']
        

