from rest_framework import serializers
from .models import Project, ContactMessage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'tech_stack',
            'github_link',
            'live_link',
            'created_date',
        ]
        read_only_fields = ['slug', 'created_date']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

    def validate_message(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Message too short."
            )
        return value