from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from ..models import Task, Project
from ..serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        if project_id:
            # If accessed through project URL
            return Task.objects.filter(project_id=project_id)
        # If accessed directly through /api/tasks/
        return Task.objects.all()

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        if project_id:
            # When creating task through project URL
            project = Project.objects.get(id=project_id)
            serializer.save(project=project)
        else:
            # When creating task directly
            project_id = self.request.data.get('project')
            if not project_id:
                raise ValidationError({'project': 'Project ID is required'})
            project = Project.objects.get(id=project_id)
            serializer.save(project=project)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'status': 'success',
                'message': 'Task retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Task not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                'status': 'success',
                'message': 'Task updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'error',
            'message': 'Invalid data provided',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                'status': 'success',
                'message': 'Task deleted successfully'
            }, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Task not found'
            }, status=status.HTTP_404_NOT_FOUND)