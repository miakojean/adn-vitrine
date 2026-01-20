from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_welcome_email(subscriber_email, subscriber_name):
    subject = "Bienvenue à la newsletter d'ADN Consulting"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [subscriber_email]
    
    # Version HTML
    html_message = render_to_string('newsletter/welcome_email.html', {'name': subscriber_name})
    
    # Version texte (ESSENTIEL)
    text_message = render_to_string('newsletter/welcome_email.txt', {'name': subscriber_name})
    
    try:
        send_mail(
            subject=subject,
            message=text_message,  # Version texte obligatoire
            from_email=from_email,
            recipient_list=to_email,
            html_message=html_message,
            fail_silently=False  # Pour voir les erreurs
        )
        return True
    except Exception as e:
        # Log l'erreur
        print(f"Erreur envoi email à {subscriber_email}: {e}")
        return False