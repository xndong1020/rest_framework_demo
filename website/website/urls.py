from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # include((pattern_list, app_namespace), namespace=None)
    path('api/blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('api/comment/', include(('comment.urls', 'comment'), namespace='comment')),
    path('api/accounts/', include(('user.urls', 'user'), namespace='user')),
    path("api/oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]
