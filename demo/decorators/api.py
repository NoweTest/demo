# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import status
import traceback

def globalExcept(method):
    def wrapper(cls,*args,**kwargs):
        try:
            result = method(cls,*args,**kwargs)
        except:
            traceback.print_exc()
            return Response({'status':'error','message':'Internal Server Error!'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return result
    return wrapper