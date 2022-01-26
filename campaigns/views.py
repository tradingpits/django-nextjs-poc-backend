from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, 
    RetrieveModelMixin, 
    # UpdateModelMixin,
    # DestroyModelMixin,
    ListModelMixin)
from rest_framework import generics, response, status
from campaigns.models import Campaign, Subscriber
from campaigns.serializers import CampaingSerializer, SubscriberSerializer


class CampaignListAPIView(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    model = Campaign
    queryset = Campaign.objects.all()
    serializer_class = CampaingSerializer


class SubscriberListAPIView(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    model = Subscriber
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class CampaignDetailAPIView(generics.GenericAPIView):
    serializer_class = CampaingSerializer
    def get(self, request, slug):
        queryset = Campaign.objects.filter(slug=slug).first()
        if queryset:
            return response.Response(self.serializer_class(queryset).data)
        return response.Response('Not found', status=status.HTTP_404_NOT_FOUND)