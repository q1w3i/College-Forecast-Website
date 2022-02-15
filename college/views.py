from college.models import Seventeen,Eighteen,Nineteen,Twenty
from college.serializers import SeventeenSerializer,EighteenSerializer,NineteenSerializer,TwentySerializer
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
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import hashlib
import json

# 自定义分页对象
class MyPageNumberPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_size = 10


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

class MyModelViewSet(ModelViewSet):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        is_valid = serializer.is_valid(raise_exception=False)
        #######
        if not is_valid:
            return Response({'code': 0, 'msg': '失败', 'data': serializer.errors})
        self.perform_update(serializer)
        ######
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({'code': 1, 'msg': '成功', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid(raise_exception=False)
        #######
        if not is_valid:
            return Response({'code': 0, 'msg': '失败', 'data': serializer.errors})
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'code': 1, 'msg': '成功', 'data': serializer.data})

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response({'code': 1, 'msg': '成功', 'data': serializer.data})
        serializer = self.get_serializer(queryset, many=True)
        return Response({'code': 1, 'msg': '成功', 'data': serializer.data})
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'code': 1, 'msg': '成功', 'data': serializer.data})
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'code': 1, 'msg': '成功', 'data': serializer.data})


class Seventeen(MyModelViewSet):
    queryset = Seventeen.objects.all()
    serializer_class = SeventeenSerializer
    pagination_class = MyPageNumberPagination
    # 局部过滤
    filter_backends = [DjangoFilterBackend]
    # filter_class = UsersFilter
    filterset_fields = ['id', 'college','grade','ranking']
    # 局部排序
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['grade','ranking' ]  # ?ordering=-currentScore  -为倒叙

class Eighteen(MyModelViewSet):
    queryset = Eighteen.objects.all()
    serializer_class = EighteenSerializer
    pagination_class = MyPageNumberPagination
    # 局部过滤
    filter_backends = [DjangoFilterBackend]
    # filter_class = UsersFilter
    filterset_fields = ['id', 'college', 'grade', 'ranking']
    # 局部排序
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['grade', 'ranking']  # ?ordering=-currentScore  -为倒叙

class Nineteen(MyModelViewSet):
    queryset = Nineteen.objects.all()
    serializer_class = NineteenSerializer
    pagination_class = MyPageNumberPagination
    # 局部过滤
    filter_backends = [DjangoFilterBackend]
    # filter_class = UsersFilter
    filterset_fields = ['id', 'college','grade','ranking']
    # 局部排序
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['grade','ranking' ]  # ?ordering=-currentScore  -为倒叙

class Twenty(MyModelViewSet):
    queryset = Twenty.objects.all()
    serializer_class = TwentySerializer
    pagination_class = MyPageNumberPagination
    # 局部过滤
    filter_backends = [DjangoFilterBackend]
    # filter_class = UsersFilter
    filterset_fields = ['id', 'college', 'grade', 'ranking']
    # 局部排序
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['grade', 'ranking']  # ?ordering=-currentScore  -为倒叙