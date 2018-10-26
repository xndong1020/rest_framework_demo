from django.urls import path, re_path
from .views import BlogpostListAPIView, BlogpostDetailAPIView, BlogpostCreateAPIView, BlogpostUpdateDeleteAPIView

urlpatterns = [
    path('', BlogpostListAPIView.as_view(), name='blog-list'),
    path('<int:pk>', BlogpostDetailAPIView.as_view(), name='blog-detail'),
    # re_path(r'^(?P<title>[a-zA-Z\s]+)/$', BlogpostDetailAPIView.as_view(), name='blog-detail-title'),
    path('create', BlogpostCreateAPIView.as_view(), name='blog-create'),
    path('edit/<int:pk>', BlogpostUpdateDeleteAPIView.as_view(), name='blog-edit'),
]
