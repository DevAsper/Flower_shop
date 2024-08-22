from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('order/', views.create_order, name='create_order'),
]
