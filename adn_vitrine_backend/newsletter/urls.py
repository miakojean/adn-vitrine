from django.urls import path
from .views import(
    SubscriberListCreateView,
    SubscriberDetailView,
    SubscriberUnsubscribeView,

    # Newsletter Views
    NewsletterListCreateView,
    NewsletterDetailView,

)

urlpatterns = [
    path('subscribers/', SubscriberListCreateView.as_view(), name="subscriber-list-create"),
    path('subscribers/<int:pk>/', SubscriberDetailView.as_view(), name="subscriber-detail"),
    path('subscribers/<int:pk>/unsubscribe/', SubscriberUnsubscribeView.as_view(), name="subscriber-unsubscribe"),

    # Newsletter Urls
    path('newsletters/', NewsletterListCreateView.as_view(), name="newsletter-list-create"),
    path('newsletters/<int:pk>/', NewsletterDetailView.as_view(), name="newsletter-detail"),
]