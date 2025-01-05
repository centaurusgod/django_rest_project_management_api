"""
URL configuration for project_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('techforing_pms.urls.users_urls')),
    path('api/projects/', include('techforing_pms.urls.projects_urls')),
    path('api/tasks/', include('techforing_pms.urls.tasks_urls')),
    path('api/comments/', include('techforing_pms.urls.comments_urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API Schema documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI - you can use either Swagger or Redoc
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    #Testing template view for github actions automation
    path('', include('test_template.urls'))
]
