from django.urls import path
from ..views.tasks import TaskListCreateView, TaskDetailView

urlpatterns = [
    # Direct task routes
    path('', TaskListCreateView.as_view(), name='task-list'),
    path('<int:id>/', TaskDetailView.as_view(), name='task-detail'),
]