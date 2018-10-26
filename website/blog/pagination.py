from rest_framework.pagination import PageNumberPagination


class BlogpostPageNumberPagination(PageNumberPagination):
    page_size = 2
