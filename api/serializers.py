from rest_framework import serializers
from api.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'dated', 'image']
