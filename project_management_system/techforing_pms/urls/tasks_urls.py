from django.urls import path
from ..views.tasks import TaskListCreateView, TaskDetailView

urlpatterns = [
    # Project-specific task endpoints
    path('projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    
    # Individual task endpoints
    path('tasks/<int:id>/', TaskDetailView.as_view(), name='task-detail'),
]