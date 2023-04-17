from rest_framework import serializers
from testapp.models import School,Student

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    school_id=serializers.ReadOnlyField()
    class Meta:
        model=School
        fields="__all__"

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Student
        fields="__all__"

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
