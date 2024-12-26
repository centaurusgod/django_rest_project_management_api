from django.urls import path, include
from ..views.projects import ProjectListCreateView, ProjectDetailView
from ..views.tasks import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='project-list-create'),  # GET all projects, POST new project
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),  # GET, PUT/PATCH, DELETE project by ID
    path('<int:project_id>/tasks/', include('techforing_pms.urls.tasks_urls')),  # include tasks urls
]