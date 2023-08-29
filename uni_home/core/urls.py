from operator import index
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('admin',admin.site.urls),
    
    
    path('seller_settings', views.seller_settings, name='settings'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('delete_post/<str:pk>', views.delete_post, name='delete_post'),
    path('landing', views.landing, name='landing'),
    path('host_landing', views.host_landing, name='host_landing'),
    
    path('post/<str:pk>', views.post, name='post'),
    path('posts_list_url', views.posts_list_url, name='posts_list_url'),
   
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('host_index',views.host_index,name='host_index'),
    
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)