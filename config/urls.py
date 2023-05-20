
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from posts.views import index,url_view,url_parameter_view,function_view,class_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/',url_view),
    #밑에 username은 경로로 받는다  
    path('url/<str:username>/',url_parameter_view),
    path('fbv/',function_view),
    path('cbv/',class_view.as_view()),
    path('',index,name='index'),
    path('posts/',include('posts.urls',namespace='posts')),
    
    path('__debug__/',include('debug_toolbar.urls')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)