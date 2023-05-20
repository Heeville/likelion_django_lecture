from django.urls import path
from .views import post_list_view,post_create_view,post_create_form_view,post_delete_view,post_delete_view,post_detail_view,post_update_view

app_name='posts'

urlpatterns=[
    path('',post_list_view,name='post_list'),
    path('new/',post_create_view,name='create'),
    #path('new/',post_create_form_view,name='create'),
    path('<int:id>/',post_detail_view,name='detail'),
    path('<int:id>/edit/',post_update_view,name='update'),
    path('<int:id>/delete/',post_delete_view,name='delete'),
]