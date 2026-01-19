from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Subscriber(models.Model):
    """Modèle pour les abonnées à la newsletter."""
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=100, blank=True, verbose_name="Prenoms")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="Nom")
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")
    unsubscribed_at = models.DateTimeField(null=True, blank=True, verbose_name="Date de désinscription")

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = "Abonné"
        verbose_name_plural = "Abonnés"

    def __str__(self):
        return self.email
    
class Newsletter(models.Model):
    """Modèle pour les newsletters"""
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('scheduled', 'Programmé'),
        ('sent', 'Envoyé'),
    ]

    title = models.CharField(max_length=200, verbose_name="Titre")
    subject= models.CharField(max_length=200, verbose_name="Sujet de l'email")
    content = models.TextField(verbose_name="Contenu")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Statut")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Créé par")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    scheduled_at = models.DateTimeField(null=True, blank=True, verbose_name="Date  d'envoi programmé")
    sent_at = models.DateTimeField(null=True, blank=True, verbose_name="Date d'envoi")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

        def __str__(self):
            return self.title
        

class Campaign(models.Model):
    """Modèle pour suivre l'envoi des newsletters"""

    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name="campaigns")
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name="campaigns")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Envoyé le")
    opened = models.BooleanField(default=False, verbose_name="Ouvert")
    opened_at = models.DateTimeField(null=True, blank=True, verbose_name="Ouvert le")
    clicked = models.BooleanField(default=False, verbose_name="Cliqué")
    clicked_at = models.DateTimeField(null=True, blank=True, verbose_name="Cliqué le")

    class Meta:
        unique_together = ['newsletter', 'subscriber']
        verbose_name = "Campagne"
        verbose_name_plural = "Campagnes"

    def __str__(self):
        return f"{self.newsletter.title} - {self.subscriber.email}"