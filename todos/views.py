from rest_framework import generics
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskGeneric(generics.GenericAPIView):
    def get(self, request):
        api_urls = {
            'List': '/list/',
            'Detail': '/detail/<str:pk>/',
            'Create': '/create/',
            'Update': '/update/<str:pk>/',
            'Delete': '/delete/<str:pk>/',
        }
        return Response(api_urls)

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdate(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'