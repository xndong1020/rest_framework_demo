from django.urls import path
from .views import get_users, get_user, create_user
# from .views import get_users, get_user, create_user, update_user

urlpatterns = [
    path('', get_users, name='user-list'),
    path('<int:pk>', get_user, name='user-detail'),
    path('create', create_user, name='user-create'),
    # path('edit/<int:pk>', update_user, name='user-edit'),
]


# from django.urls import path
# from .views import UserAPIView
#
# urlpatterns = [
#     path('', UserAPIView.as_view(), name='user-list'),
#     path('<int:pk>', UserAPIView.as_view(), name='user-detail'),
#     path('create', UserAPIView.as_view(), name='user-create'),
#     path('edit/<int:pk>', UserAPIView.as_view(), name='user-edit'),
# ]
