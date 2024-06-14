from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    academic_achievements = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    documents = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Portfolio {self.id}'
