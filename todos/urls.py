from django.urls import path
from .import views

urlpatterns = [
    path('', views.TaskGeneric.as_view(), name='generic'),
    path('list/', views.TaskList.as_view(), name='list'),
    path('detail/<str:pk>/', views.TaskDetail.as_view(), name='detail'),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path('update/<str:pk>/', views.TaskUpdate.as_view(), name='create'),
    path('delete/<str:pk>/', views.TaskDelete.as_view(), name='delete'),
]


