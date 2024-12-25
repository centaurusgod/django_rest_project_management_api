from enum import unique
from django.db import models
import os
from datetime import datetime
import hashlib
import binascii

# Create your models here.

#ensure encyrption in the Users password when saving
    
class User(models.Model):
#  I‘d: Primary Key
# Username: String (Unique)
# Email: String (Unique)
# Password: String
# First_name: String
# Last_name: String
# Date_joined: DateTime
    username = models.CharField(max_length=150, unique=True)  
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=255) 
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.username 

    def save(self, *args, **kwargs):
        self.password = self._hash_password(self.password)
        super().save(*args, **kwargs)

    def _hash_password(self, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return binascii.hexlify(key).decode('utf-8')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Project(models.Model):
#     I‘d: Primary Key
# Name: String
# Description: Text
# Owner: Foreign Key (to Users)
# Created_at: DateTime
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'   

class ProjectMember(models.Model):
#     I’d: Primary Key
# Project: Foreign Key (to Projects)
# User: Foreign Key (to Users)
# Role: String (Admin, Member)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.role}"    

    class Meta:
        verbose_name = 'Project Member'
        verbose_name_plural = 'Project Members'   


class Task(models.Model):
# Tasks: Store task details.
# I’d: Primary Key
# Title: String
# Description: Text
# Status: String (To Do, In Progress, Done)
# Priority: String (Low, Medium, High)
# Assigned_to: Foreign Key (to Users, nullable)
# Project: Foreign Key (to Projects)
# Created_at: DateTime
# Due_date: DateTime

    STATUS_CHOICES = [
    ("to_do", "To Do"),
    ("in_progress", "In Progress"),
    ("done", "Done")
]

    PRIORITY_CHOICES = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    

    def __str__(self):
        return f"{self.title} - {self.project.name} - {self.priority} - {self.status}" 

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'   

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'   
