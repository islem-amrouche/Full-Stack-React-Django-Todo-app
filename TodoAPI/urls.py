from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', TodoView.as_view(), name="todos"),
    path('update/<str:pk>/', UpdateTodo, name="update"),
    path('delete/<str:pk>/', DeleteTodo, name="delete"),
    path('check/<str:pk>/', CheckTodo, name="check"),
]