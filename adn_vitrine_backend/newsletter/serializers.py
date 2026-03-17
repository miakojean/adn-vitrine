from rest_framework import serializers
from .models import Newsletter, Subscriber, Campaign

class SubscriberSerializer(serializers.ModelSerializer):
    """Serializer pour les abonnées"""
    class Meta:
        model = Subscriber
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'subscribed_at', 'unsubscribed_at']
        read_only_fields = ['id', 'subscribed_at', 'unsubscribed_at']

class NewsletterSerializer(serializers.ModelSerializer):
    """Serializer pour les newsletters"""
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Newsletter
        fields = [
            'id', 
            'title', 
            'subject', 
            'content', 
            'status', 
            'created_by', 
            'created_by_username', 
            'created_at', 
            'updated_at', 
            'scheduled_at', 
            'sent_at'
        ]
        read_only_fields = [
            'id', 
            'created_at', 
            'updated_at', 
            'sent_at', 
            'created_by_username'
        ]

class CampaignSerializer(serializers.ModelSerializer):
    """Serializer pour les campagnes"""
    newsletter_title = serializers.CharField(source='newsletter.title', read_only=True)
    subscriber_email = serializers.CharField(source='subscriber.email', read_only=True)

    class Meta:
        model = Campaign
        fields = [
            'id', 'newsletter', 'newsletter_title', 'subscriber', 'subscriber_email',
            'sent_at', 'opened', 'opened_at', 'clicked', 'clicked_at'
        ]
        read_only_fields = [
            'id', 'sent_at', 'opened_at', 'clicked_at', 
            'newsletter_title', 'subscriber_email'
        ]

