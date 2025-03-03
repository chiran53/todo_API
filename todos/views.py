from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
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

class Taskpagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskList(generics.ListAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    pagination_class = Taskpagination

    def get_queryset(self):
        queryset = super().get_queryset()

        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)

        priority = self.request.query_params.get('priority', None)
        if priority:
            queryset = queryset.filter(priority=priority)
        return queryset

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