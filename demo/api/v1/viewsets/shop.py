# -*- coding: utf-8 -*-
from rest_framework import serializers, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import status


# 这是我喜欢的import方式，有两个好处。
# 1.可以避免变量混淆。毕竟common可能和本文件代码中的其他变量名相同，这样能让你你在coding的过程中变量名使用更加自由。
# 2.import 后的路径可以帮助其他开发定位我引用的代码位置。当然用PyCharm的人没有这个问题=。=。
# 所以你可以按照自己喜欢的来。
# 参考: https://docs.python.org/2/tutorial/modules.html

import demo.demo.models as demo_models
import demo.decorators.api as decorators
import demo.api.serializers as serializers

class FruitViewSet(viewsets.ModelViewSet):
    filter_fields = ('name','price',)

    queryset = demo_models.fruit.objects.all()
    serializer_class = serializers.FruitSerializer
    lookup_field = 'name'


class OrderViewSet(viewsets.ModelViewSet):
    filter_fields = ('customer',)

    queryset = demo_models.order.objects.all().order_by('-id')
    serializer_class = serializers.OrderSerializer

    # 浏览器内用console调用 $.ajax({type:'post','url':"http://127.0.0.1:8091/api/v1/order/newOrder/",data:{'fruit_id':'1','amount':2,'customer':'qi.feng'}})
    @list_route(methods=['post'])
    @decorators.globalExcept
    def newOrder(self,request):
    	print request.POST
        requiredFields = ['fruit_id','amount','customer']
        for field in requiredFields:
            if not request.POST.get(field,None):
                return Response({'status':'error','message':'%s is null!' % field},status=status.HTTP_400_BAD_REQUEST)

        order = demo_models.order(
            fruit = demo_models.fruit.objects.get(id=int(request.POST.get('fruit_id'))),
            amount = int(request.POST.get('amount')),
            customer = request.POST.get('customer')
        )
        order.save()

        return Response({'status':'ok'})

    # 浏览器内用console调用 $.ajax({type:'post','url':"http://127.0.0.1:8091/api/v1/order/1/change/",data:{'fruit_id':'2','amount':4}})
    @detail_route(methods=['post'])
    @decorators.globalExcept
    def change(self,request,pk=None):
        obj = self.get_object()

        fruit_id = request.POST.get('fruit_id',None)
        amount = request.POST.get('amount',None)

        fruits = demo_models.fruit.objects.filter(id=int(fruit_id))
        if fruits:
            obj.fruit = fruits[0]
        else:
            return Response({'status':'error','message':'Invalid fruit id!'},status=status.HTTP_400_BAD_REQUEST)

        obj.amount = amount if int(amount) >= 0 else obj.amount
        obj.save_result()

        return Response({'status':'ok'})

