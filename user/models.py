from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Todo(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task_name=models.CharField(max_length=120)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.created_by.first_name