# -*- coding: utf-8 -*-
from rest_framework import serializers

import demo.demo.models as demo_models

class FruitSerializer(serializers.ModelSerializer):
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = demo_models.fruit


class OrderSerializer(serializers.ModelSerializer):
    fruit = FruitSerializer()
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    totalPrice = serializers.SerializerMethodField()

    class Meta:
        model = demo_models.order

    def get_totalPrice(self, obj):
        return obj.fruit.price * obj.amount