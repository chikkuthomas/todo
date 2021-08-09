from django.db import models

# Create your models here.
class Completed(models.Model):
    completed=models.CharField(max_length=12,unique=True)
    def __str__(self):
        return self.completed

class Todo(models.Model):
    created_by = models.CharField(max_length=120)
    task_name=models.CharField(max_length=120)
    completed=models.ForeignKey(Completed,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.created_by