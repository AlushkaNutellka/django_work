from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskListSerializer
from rest_framework.response import Response
from .serializers import TaskSerializer


@api_view(['GET'])
def task_list(request):
    queryset = Task.objects.all()
    print(queryset)
    serializer = TaskListSerializer(queryset
                                    , many=True)
    return Response(serializer.data,
                    status=200)


@api_view(['GET'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data,
                        status=200)

    except Task.DoesNotExist:
        return Response(f'ЭЙ ТАКОГО НЕТУ,ТЫ ОШИБСЯ {pk}',
                        status=404)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,
                    status=201)


@api_view(['PUT', 'PATCH'])
def task_update(request, pk):
    try:
        task = Task.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = TaskSerializer(instance=task, data=request.data)
        else:
            serializer = TaskSerializer(instance=task, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=206)
    except Task.DoesNotExist:
            return Response(f'This task {pk},'f'does not exist',
                            status=404)


@api_view(['DELETE'])
def task_delete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response({'msg': 'Deleted successfully'},
                        status=204)
    except Task.DoesNotExist:
        return Response(f'This task {pk},'f'does not exist',
                        status=404)
