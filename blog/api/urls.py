from django.urls import path

from blog.api.views import api_blog_detail_view,api_blog_update_view,api_blog_delete_view,api_blog_create_view


app_name='blog_api'

urlpatterns = [

        path('<slug>/',api_blog_detail_view,name='api_detail'),
        path('update/<slug>/',api_blog_update_view,name='api_update'),
        path('delete/<slug>/',api_blog_delete_view,name='api_delete'),
        path('create/',api_blog_create_view,name='api_create'),

]