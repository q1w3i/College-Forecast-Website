from grade.models import Grade
from grade.serializers import GradeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet,ModelViewSet,ReadOnlyModelViewSet

import json

class MyListView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        # 重写response 返回信息
        response = {'code': 1, 'msg': '查询成功'}

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # 将原来的结果放进response字典
        print(serializer.data[0])
        response['data'] = serializer.data
        return Response(response)


class Grade(MyListView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def get(self,request):
        return self.list(request)
