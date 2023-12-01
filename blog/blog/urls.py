from django.contrib import admin
from django.urls import path, include
from migass.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('notadm/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact48945894759486/', contact, name='contact'),
    path('post/<slug:post_slug>/', single_post, name='single-post'),
    path('editor/<int:pk>/', Editor.as_view(), name='editor'),
    path('editor/', CreatePost.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='general/login.html'), name='login'),
    path('logout/', loggout, name='logout'),
    path('register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
