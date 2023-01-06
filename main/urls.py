from django.contrib import admin
from django.urls import path
from main.views import task_list, task_detail, task_create, task_delete, task_update

urlpatterns = [
    path('tasks/', task_list),
    path('tasks/<int:pk>', task_detail),
    path('tasks_create/', task_create),
    path('tasks_update/<int:pk>/', task_update),
    path('tasks_delete/<int:pk>/', task_delete)

]