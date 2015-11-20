# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
import viewsets.shop as shop


router = routers.DefaultRouter()
router.register(r'fruit', shop.FruitViewSet)
router.register(r'order', shop.OrderViewSet)


urlpatterns = patterns('demo.api.views',
    url(r'^', include(router.urls)),
)