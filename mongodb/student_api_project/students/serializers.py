from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    which_class = serializers.IntegerField()
    age = serializers.IntegerField()

    def create(self, validated_data):
        # Create and return a new 'Students' instance, given the validated data
        return Students(**validated_data).save()

    def update(self, instance, validated_data):
        # Update and return an existing 'Students' instance, given the validated data
        instance.student_id = validated_data.get('student_id', instance.student_id)
        instance.name = validated_data.get('name', instance.name)
        instance.which_class = validated_data.get('which_class', instance.which_class)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
