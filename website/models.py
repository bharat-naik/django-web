from django.db import models

# Create your models here.


class Message(models.Model):
	nm=models.CharField(max_length=30)
	txt=models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.nm
	
