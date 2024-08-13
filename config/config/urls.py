from django.contrib import admin
from django.urls import path
from core.views import example
from core.views import reg
from django.conf import settings
from django.conf.urls.static import static
from blog.views import posts_list
from blog.views import post_like
from playlist.views import video_list
from playlist.views import video_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', example),
    path('reg/', reg),
    path('blog/posts_list/', posts_list, name='posts_list'),
    path('blog/post_like/', post_like, name='post_like'),
    path('playlist/video_list/', video_list, name='video_list'),
    path('playlist/video_create', video_create),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

