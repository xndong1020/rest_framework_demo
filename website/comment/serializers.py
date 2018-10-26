from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Comment


class CommmentSerializer(ModelSerializer):
    user = SerializerMethodField()
    post = SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_post(self, obj):
        return obj.post.title

    class Meta:
        model = Comment
        fields = ('id', 'content', 'user', 'post',)
