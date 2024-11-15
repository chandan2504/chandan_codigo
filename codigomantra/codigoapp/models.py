from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length = 150)
	description = models.TextField()
	author = models.CharField(max_length = 100)
	like = models.IntegerField(default = 0)

	def __str__(self):
		return self.title
	

