from django.contrib import admin
from django.urls import path

from campaigns import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'campaigns', views.CampaignListAPIView)
router.register(r'subscribers', views.SubscriberListAPIView)


urlpatterns = [
     path('campaign/<str:slug>', views.CampaignDetailAPIView.as_view(), name='api_campaign_detail'),
]

urlpatterns += router.urls
