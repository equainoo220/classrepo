from .models import Student 
from rest_framework import serializers

# This is where we convert our models
# json format by serializing it

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'