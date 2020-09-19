from django.urls import path, include
from . import views

app_name='post'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>/', views.detail, name='detail'),
]
