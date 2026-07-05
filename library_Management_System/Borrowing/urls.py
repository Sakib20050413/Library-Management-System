from django.urls import path
from . import views

urlpatterns = [
    path('', views.borrowing_list, name='borrowing_list'),
    path('<int:pk>/', views.borrowing_detail, name='borrowing_detail'),
]