from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_post_view, name='post_list'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
]
