from django.urls import path
from ..views.projects import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),  # GET all projects, POST new project
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),  # GET, PUT/PATCH, DELETE project by ID
]