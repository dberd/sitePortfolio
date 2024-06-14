from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='')
    full_name = models.CharField(max_length=200, default='')
    about_me = models.TextField(default='')
    course_work = models.TextField(default='')
    conferences = models.TextField(default='')
    practices = models.TextField(default='')
    skills = models.TextField(default='')
    extracurricular_activities = models.TextField(default='')
    documents = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Portfolio {self.id}'
