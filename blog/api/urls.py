from django.urls import path
from . import views
from .views import UserList,UserDetail,PostList,PostDetail
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('users/',UserList.as_view(),name='user_list'),
    path('users/<int:pk>/',UserDetail.as_view(),name='user_detail'),
    path('posts/',PostList.as_view()),
    path('posts/<int:pk>/',PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns=format_suffix_patterns(urlpatterns)