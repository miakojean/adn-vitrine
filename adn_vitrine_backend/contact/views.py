from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from newsletter.utils import send_welcome_email
from .models import ContactMessage
from .serializers import ContactMessageSerializer
# Create your views here.

class ContactMessageCreateView(APIView):
    """
    Docstring for ContactMessageCreateView
    """
    def post(self, request):
        """Créer un nouveau message de contact"""
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)