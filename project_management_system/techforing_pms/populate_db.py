import os
import sys
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_management_system.settings')
django.setup()

from techforing_pms.models import User, Project, ProjectMember, Task, Comment

def create_users():
    users = []
    for i in range(1, 11):
        user = User.objects.create(
            username=f'user{i}',
            email=f'user{i}@example.com',
            password='password123',  # This will be hashed by the save method
            first_name=f'First{i}',
            last_name=f'Last{i}'
        )
        users.append(user)
    return users

def create_projects(users):
    projects = []
    statuses = ['todo', 'in_progress', 'done']
    
    for i in range(1, 11):
        project = Project.objects.create(
            name=f'Project {i}',
            description=f'This is a description for Project {i}',
            status=random.choice(statuses),
            owner=random.choice(users),
            created_at=timezone.now() - timedelta(days=random.randint(1, 30))
        )
        projects.append(project)
    return projects

def create_project_members(users, projects):
    roles = ['Admin', 'Member']
    for project in projects:
        # Assign 2-3 members per project
        for _ in range(random.randint(2, 3)):
            ProjectMember.objects.create(
                project=project,
                user=random.choice(users),
                role=random.choice(roles)
            )

def create_tasks(users, projects):
    tasks = []
    statuses = ['to_do', 'in_progress', 'done']
    priorities = ['low', 'medium', 'high']
    
    for i in range(1, 11):
        task = Task.objects.create(
            title=f'Task {i}',
            description=f'This is a description for Task {i}',
            status=random.choice(statuses),
            priority=random.choice(priorities),
            assigned_to=random.choice(users),
            project=random.choice(projects),
            created_at=timezone.now() - timedelta(days=random.randint(1, 15)),
            due_date=timezone.now().date() + timedelta(days=random.randint(1, 30))
        )
        tasks.append(task)
    return tasks

def create_comments(tasks):
    for task in tasks:
        # Create 10 comments for each task
        for i in range(1, 11):
            Comment.objects.create(
                content=f'Comment {i} on {task.title}: This is a sample comment.',
                created_at=timezone.now() - timedelta(days=random.randint(1, 10)),
                task=task
            )

def main():
    # Clear existing data
    Comment.objects.all().delete()
    Task.objects.all().delete()
    ProjectMember.objects.all().delete()
    Project.objects.all().delete()
    User.objects.all().delete()

    print("Creating users...")
    users = create_users()
    
    print("Creating projects...")
    projects = create_projects(users)
    
    print("Creating project members...")
    create_project_members(users, projects)
    
    print("Creating tasks...")
    tasks = create_tasks(users, projects)
    
    print("Creating comments...")
    create_comments(tasks)
    
    print("Database population completed successfully!")

if __name__ == '__main__':
    main()
