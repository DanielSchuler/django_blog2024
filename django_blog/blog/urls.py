from django.urls import path
from .views import post_list,post_detail,posts_by_category

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),
]
