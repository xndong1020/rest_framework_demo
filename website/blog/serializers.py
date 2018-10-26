from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from .models import Blogpost
from comment.models import Comment
from comment.serializers import CommmentSerializer


class BlogpostSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='blog:blog-detail', lookup_field='pk')
    user = SerializerMethodField()
    comments = SerializerMethodField()

    def get_comments(self, obj):
        comments_queryset = Comment.objects.all()
        comments = CommmentSerializer(comments_queryset, many=True).data
        return comments

    def get_user(self, obj):
        return {
            'id': obj.user.id,
            'username': obj.user.username
        }

    class Meta:
        model = Blogpost
        fields = [
            'url',
            'title',
            'author',
            'body',
            'comments',
            'user',
        ]
