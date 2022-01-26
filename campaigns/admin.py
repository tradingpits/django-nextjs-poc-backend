from django.contrib import admin
from campaigns.models import Campaign, Subscriber

class CampaignModelAdmin(admin.ModelAdmin):
    list_display=('title', 'created_at', 'updated_at')
    search_fields=('title', 'description')

class SubscriberModelAdmin(admin.ModelAdmin):
    list_display=('email', 'created_at', 'campaign')
    search_fields=('email', 'campaign__title',)

    # @admin.display(ordering='campaign__author', description='Campaign')
    # def campaign_title(self, obj):
    #     return obj.campaign.title

# Register your models here.
admin.site.register(Campaign, CampaignModelAdmin)
admin.site.register(Subscriber, SubscriberModelAdmin)
