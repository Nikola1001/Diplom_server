from rest_framework import serializers

from .models import Process

class ProcessSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    history = serializers.CharField()
    suspicious_processes = serializers.CharField()
    all_processes = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Process.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.history = validated_data.get('history', instance.history)
        instance.suspicious_processes = validated_data.get('suspicious_processes', instance.suspicious_processes)
        instance.all_processes = validated_data.get('all_processes', instance.all_processes)
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.save()
        return instance