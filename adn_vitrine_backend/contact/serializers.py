from .models import ContactMessage
from rest_framework import serializers


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            'id',
            'name',
            'phone_number',
            'email',
            'subject',
            'message',
        ]
        read_only_fields = ['id']
