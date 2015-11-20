# -*- coding: utf-8 -*-
from django.db import models
import datetime

"""
这里是demo业务相关的model类。
"""

"""
以下是虚model类，作为父类来使用，是所有子类都会拥有以下三个参数。
值得一提的是，updatedseq的作用是在并发读写的时候用来防止脏数据的产生。
每次存数据的时候通过update id+updatedseq数据匹配来保证写数据的准确，且不会覆盖在当前进程读数据之后已经被写入的变化。
"""
class common_column(models.Model):
    class Meta:
        abstract = True

    createdtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)
    updatedseq = models.IntegerField(default=0)

    def save_result(self):
        fields = self._meta.get_all_field_names()
        fieldsValue = {}
        for field in fields:
            fieldsValue[field] = getattr(self,field)

        fieldsValue['updatedseq'] += 1
        fieldsValue['updatedtime'] = datetime.datetime.now()

        rows = type(self).objects.filter(id=self.id,updatedseq=self.updatedseq).update(**fieldsValue)

        if rows:
            self.updatedseq += 1

        return rows

class fruit(common_column):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255) #django 1.8开始charfield的max_length超过255，在通过mitgrate建表的时候会报不能超过255的错。

class order(common_column):
    fruit = models.ForeignKey(fruit)
    amount = models.IntegerField(default=0)
    customer = models.CharField(max_length=100)