from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [



    #ViewSet
    # path('tasks/', TaskViewSet.as_view({'get':'list'})),
    # path('tasks/<int:pk>/', TaskViewSet.as_view({'get':'list'}))


    #Generics
    # path('tasks/', TaskListCreateView.as_view()),
    # path('tasks/<int:pk>/', TaskDetailView.as_view())



    #Api views
    # path('tasks/', TaskListCreateApiView.as_view()),
    # path('tasks/<int:pk>/', TaskDetailApiView.as_view()),




    # funck views
    # path('tasks/', task_list),
    # path('tasks/<int:pk>', task_detail),
    # path('tasks_create/', task_create),
    # path('tasks_update/<int:pk>/', task_update),
    # path('tasks_delete/<int:pk>/', task_delete)

]

urlpatterns += router.urls
