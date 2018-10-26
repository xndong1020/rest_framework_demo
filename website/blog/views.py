from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsResourceOwnerOrAdminUser
from .pagination import BlogpostPageNumberPagination
from .models import Blogpost
from .serializers import BlogpostSerializer


class BlogpostListAPIView(ListAPIView):
    queryset = Blogpost.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogpostSerializer
    # filter_backends = [SearchFilter, OrderingFilter]
    # search_fields = ['title', 'body', 'author', 'user__first_name', 'user__last_name']
    # pagination_class = BlogpostPageNumberPagination

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Blogpost.objects.all()
    #     query = self.request.GET.get('q')
    #
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(title__icontains=query) |
    #             Q(body__icontains=query) |
    #             Q(author__icontains=query) |
    #             Q(user__first_name__icontains=query) |
    #             Q(user__last_name__icontains=query)
    #         ).distinct()
    #     return queryset_list


class BlogpostDetailAPIView(RetrieveAPIView):
    queryset = Blogpost.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BlogpostSerializer
    # lookup_field = 'title'


class BlogpostCreateAPIView(CreateAPIView):
    queryset = Blogpost.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogpostSerializer


class BlogpostUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """
    use RetrieveUpdateDestroyAPIView not UpdateAPIView to prefill the form
    """
    queryset = Blogpost.objects.all()
    permission_classes = (IsResourceOwnerOrAdminUser,)
    serializer_class = BlogpostSerializer
