from rest_framework import serializers

# https://stackoverflow.com/questions/26593312/optimizing-database-queries-in-django-rest-framework

from .models import (
    Campaign, 
    Subscriber
    )


class CampaingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    campaigns = CampaingSerializer(read_only=True, many=True)

    class Meta:
        model = Subscriber
        fields = '__all__'

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.prefetch_related("campaigns")

        return queryset