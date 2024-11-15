from rest_framework import serializers
from .models import Blog

class blogserializer(serializers.ModelSerializer):
	class Meta:
		model = Blog 
		# feilds = ["id","title","description","author"]
		fields = '__all__'