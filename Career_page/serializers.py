from .models import Job
from rest_framework import serializers
from rest_framework import serializers


class JobSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=200)
    summary = serializers.CharField()
    department = serializers.CharField(max_length=100)
    description = serializers.CharField()

    vacancies = serializers.IntegerField()
    location = serializers.CharField(max_length=200)

    min_exp = serializers.IntegerField()
    max_exp = serializers.IntegerField()

    edu_requirment = serializers.CharField()
    skill_requirment = serializers.CharField()

    min_salary = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    max_salary = serializers.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    job_type = serializers.CharField(max_length=100)
    work_mode = serializers.CharField(max_length=100)

    job_post_date = serializers.DateTimeField()
    end_apply_date = serializers.DateTimeField()

    status = serializers.CharField(max_length=50)
    def create(self,validated_data):
        return Job.objects.create(**validated_data)
    def update(self,instance,validated_data):
        for field,value in validated_data.items():
            setattr(instance,field,value)
        instance.save() 
        return instance
