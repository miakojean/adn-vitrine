from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Subscriber, Newsletter, Campaign
from .serializers import SubscriberSerializer, NewsletterSerializer, CampaignSerializer

# Create your views here.
class SubscriberListCreateView(APIView):
    """Liste tous les abonnés et crée un nouvel abonné."""

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get(self, request):
        """Récupérer tous les abonnés"""
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        """Créer un nouvel abonné"""
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubscriberDetailView(APIView):
    """Récupère, met à jour ou supprime un abonné"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Récupérer un abonné spécifique"""
        subscriber = get_object_or_404(Subscriber, pk=pk)
        serializer = SubscriberSerializer(subscriber)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        """Mettre à jour un abonné"""
        subscriber = get_object_or_404(Subscriber, pk=pk)
        serializer = SubscriberSerializer(subscriber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Supprimer un abonné"""

        subscriber = get_object_or_404(Subscriber, pk=pk)
        subscriber.delete()
        return Response(
            {'message':'Abonné supprimé avec succès.'},
            status=status.HTTP_204_NO_CONTENT
        )
    
class SubscriberUnsubscribeView(APIView):
    """Désabonner un abonné"""
    permission_classes = [AllowAny]

    def post(self, request, pk):
        """Desabonner un abonné"""

        subscriber = get_object_or_404(Subscriber, pk=pk)
        subscriber.is_active = False
        subscriber.unsubscribed_at = timezone.now()
        subscriber.save()
        return Response(
            {'message':'Vous avez été désabonné avec succès.'},
            status=status.HTTP_200_OK
        )
# ===================== newsletter Views =====================

class NewsletterListCreateView(APIView):
    """Liste de toutes les newsletters et crée une nouvelle newsletter"""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Récupérer toutes les newsletters"""
        newsletters = Newsletter.objects.all()
        serializer = NewsletterSerializer(newsletters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Créer une nouvelle newsletter"""
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NewsletterDetailView(APIView):
    """Récupère, met à jour ou supprime une newsletter"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """Récupérer une newsletter spécifique"""
        newsletter = get_object_or_404(Newsletter, pk=pk)
        serializer = NewsletterSerializer(newsletter)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        """Mettre à jour une newsletter"""
        newsletter = get_object_or_404(Newsletter, pk=pk)
        serializer = NewsletterSerializer(newsletter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Supprimer une newsletter"""
        newsletter = get_object_or_404(Newsletter, pk=pk)
        newsletter.delete()
        return Response(
            {'message':'Newsletter supprimée avec succès.'},
            status=status.HTTP_204_NO_CONTENT
        )
    
class NewsletterSendView(APIView):
    """Récupérer toutes les newsletters en brouillon"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Liste des brouillons"""
        drafts = Newsletter.objects.filter(status='draft')
        serializer = NewsletterSerializer(drafts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        """Supprimer une campagne"""
        compaign = get_object_or_404(Campaign, pk=pk)
        serializer = CampaignSerializer(compaign)
        return Response(serializer.data, status=status.HTTP_200_OK)