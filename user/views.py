from rest_framework import exceptions,generics,mixins,status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
class TestView(APIView):
  logger = logging.getLogger('main')
  def get(self,request,*args,**kwargs):
    self.logger.info("xxxxxx")
    return Response({})








