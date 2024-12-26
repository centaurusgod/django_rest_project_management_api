from django.urls import path
from ..views.users import UserListView, UserDetailView, RegisterUserView, LoginUserView
urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),                # GET all users
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),   # GET, PUT/PATCH, DELETE user by ID
    path('register/', RegisterUserView.as_view(), name='user-register'),  # POST: Register user
    path('login/', LoginUserView.as_view(), name='user-login'),        # POST: Login user
]
