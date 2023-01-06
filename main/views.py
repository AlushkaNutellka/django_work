from django.shortcuts import render
# from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskListSerializer
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from .serializers import TaskListSerializer, TaskSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
#
# class TaskListCreateApiView(APIView):
#     def get(self, request):
#         queryset = Task.objects.all()
#         serializer = TaskListSerializer(
#             instance=queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = TaskSerializer(data=
#                                         request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=201)
#
#
# class TaskDetailApiView(APIView):
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(id=pk)
#         except Task.DoesNotExist:
#             raise Http404
#
#     def get(self, requests, pk):
#         queryset = self.get_object(pk)
#         serializer = TaskSerializer(requests)
#         return Response(serializer.data,
#                         status=200)
#
#     def put(self, request, pk):
#         queryset = self.get_object(pk)
#         serializer = TaskSerializer(queryset,
#                                     instance=queryset,
#                                     data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # queryset.title = request.data['title']
#         return Response(serializer.data,
#                         status=200)
#
#     def deleted(self, request, pk):
#         queryset = self.get_object()
#         queryset.delete()
#         return Response({'msg':'Successfully deleeted '}, status=200)
#
#=====================================================================================================
#CRUD - get, post, delete, put, patch
#create, read, update, delete




# class TaskList(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskDetailViews(generics.RetrieveAPIView):
#     queryset = Task.objects.all()
#     serialize_class = TaskSerializer
#
#
# class TaskListCreateView(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return TaskSerializer
#         return TaskSerializer
#
#
# class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#==============================================================================

#ViewSet, ModelViewSet
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer








# """========================================================================================="""
# @api_view(['GET'])
# def task_list(request):
#     queryset = Task.objects.all()
#     print(queryset)
#     serializer = TaskListSerializer(queryset
#                                     , many=True)
#     return Response(serializer.data,
#                     status=200)
#
#
# @api_view(['GET'])
# def task_detail(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data,
#                         status=200)
#
#     except Task.DoesNotExist:
#         return Response(f'ЭЙ ТАКОГО НЕТУ,ТЫ ОШИБСЯ {pk}',
#                         status=404)
#
#
# @api_view(['POST'])
# def task_create(request):
#     serializer = TaskSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data,
#                     status=201)
#
#
# @api_view(['PUT', 'PATCH'])
# def task_update(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         if request.method == 'PUT':
#             serializer = TaskSerializer(instance=task, data=request.data)
#         else:
#             serializer = TaskSerializer(instance=task, data=request.data, partial=True)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=206)
#     except Task.DoesNotExist:
#             return Response(f'This task {pk},'f'does not exist',
#                             status=404)
#
#
# @api_view(['DELETE'])
# def task_delete(request, pk):
#     try:
#         task = Task.objects.get(id=pk)
#         task.delete()
#         return Response({'msg': 'Deleted successfully'},
#                         status=204)
#     except Task.DoesNotExist:
#         return Response(f'This task {pk},'f'does not exist',
#                         status=404)
