from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..models import Project
from ..serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status

# Projects
# List Projects (GET /api/projects/): Retrieve a list of all projects.
# Create Project (POST /api/projects/): Create a new project.
# Retrieve Project (GET /api/projects/{id}/): Retrieve details of a specific project.
# Update Project (PUT/PATCH /api/projects/{id}/): Update project details.
# Delete Project (DELETE /api/projects/{id}/): Delete a project.

class ProjectListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    
    def get(self, request, *args, **kwargs):
        # This shows how list() works internally
        projects = self.get_queryset()
        serializer = self.get_serializer(projects, many=True)
        return Response({
            'status': 'success',
            'message': 'Projects retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Project created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'message': 'Invalid data provided',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get(self, request, *args, **kwargs):
        # This shows how retrieve() works internally
        instance = self.get_object()
        if not instance:
            return Response({
                'status': 'error',
                'message': 'Project not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance)
        return Response({
            'status': 'success',
            'message': 'Project retrieved successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({
                'status': 'error',
                'message': 'Project not found'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Project updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': 'error',
            'message': 'Invalid data provided',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({
                'status': 'error',
                'message': 'Project not found'
            }, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({
            'status': 'success',
            'message': 'Project deleted successfully'
        }, status=status.HTTP_200_OK)
