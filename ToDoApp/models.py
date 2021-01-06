from django.db import models

# Create your models here.
class Tasks(models.Model):
	title = models.CharField(max_length=200)
	date = models.DateField()
	time = models.TimeField(auto_now=False, auto_now_add=False)
	complete=models.BooleanField(default=False)
	expired=models.BooleanField(default=False)
	
	class Meta:
		db_table="Tasks"
		