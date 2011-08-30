from django.db import models

# Create your models here.
class Todo(models.Model):
	all_done = models.BooleanField()
	todo_name = models.CharField(max_length=160)
	date_added = models.DateTimeField(auto_now_add=True)
	date_due = models.DateTimeField()
	
class Subtask(models.Model):
	task_name = models.CharField(max_length=160)
	done = models.BooleanField()