from django.contrib import admin
from .models import Subscriber, Newsletter, Campaign
# Register your models here.

admin.site.register(Subscriber)
admin.site.register(Newsletter)
admin.site.register(Campaign)
