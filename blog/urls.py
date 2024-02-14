from django.urls import path
from . import views

urlpatterns = [
    path('', views.signUp, name='signUp'),
    path('signIn', views.signIn, name='signIn'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_new', views.post_new, name='post_new'),
    path('post_edit/<int:pk>', views.post_edit, name='post_edit'),
]








