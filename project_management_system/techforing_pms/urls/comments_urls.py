from django.urls import path
from ..views.comments import CommentListCreateView, CommentDetailView

urlpatterns = [
    # Task-specific comment endpoints
    path('tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    
    # Individual comment endpoints
    path('comments/<int:id>/', CommentDetailView.as_view(), name='comment-detail'),
]