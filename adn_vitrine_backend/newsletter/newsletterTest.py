#!/usr/bin/env python
import os
import sys
import django

# 1. Ajouter le chemin de votre projet au PYTHONPATH
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)

# 2. Définir le module de settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adn_vitrine_backend.settings')

# 3. Initialiser Django
try:
    django.setup()
    print("✅ Django initialisé avec succès")
except Exception as e:
    print(f"❌ Erreur lors de l'initialisation de Django: {e}")
    sys.exit(1)

# 4. Maintenant vous pouvez importer et utiliser settings
from django.conf import settings
from django.core.mail import send_mail

print("🔧 Configuration actuelle :")
print(f"  EMAIL_HOST: {getattr(settings, 'EMAIL_HOST', 'Non défini')}")
print(f"  EMAIL_PORT: {getattr(settings, 'EMAIL_PORT', 'Non défini')}")
print(f"  EMAIL_HOST_USER: {getattr(settings, 'EMAIL_HOST_USER', 'Non défini')}")

# Test d'envoi d'email
try:
    send_mail(
        subject='Test Newsletter',
        message='Ceci est un test d\'envoi de newsletter.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['miakojeanyves@gmail.com'],
        fail_silently=False,
    )
    print("✅ Email envoyé avec succès !")
except Exception as e:
    print(f"❌ Erreur lors de l'envoi: {e}")