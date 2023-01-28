from rest_framework import serializers
from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('first_name','last_name','cohort','fav_language','capstone')