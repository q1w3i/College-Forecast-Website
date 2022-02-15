import django_filters.rest_framework
from users.models import User
from users.models import UpdateUser
from users.serializers import UserSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet,ModelViewSet,ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import hashlib

# 自定义分页对象
class MyPageNumberPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_size = 20
    max_page_size = 10

# class UsersFilter(django_filters.rest_framework.FilterSet):
#     name = django_filters.CharFilter(field_name="targetCollege")
#     class Meta:
#         model = User  # 关联的表
#         fields = ["targetCollege"]  # 过滤的字段

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



class UsersAll(MyModelViewSet):

    pagination_class = PageNumberPagination # ?page=4&page_size=100

    queryset = UpdateUser.objects.all()
    serializer_class = UserSerializer
    # 自定义分页类
    pagination_class = MyPageNumberPagination
    # 局部过滤
    filter_backends = [DjangoFilterBackend]
    # filter_class = UsersFilter
    filterset_fields = ['id', 'targetColleges']
    # 局部排序
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['currentScore',]#?ordering=-currentScore  -为倒叙

    @action(methods=["PUT"],detail=True)
    # 前缀/参数/方法名
    def update_user(self,request,pk):
        # 1,获取参数
        user = self.get_object()
        data = request.data
        # 2,创建序列化器
        serializer = self.get_serializer(instance=user, data=data, partial=True)
        # 3,校验,入库
        is_valid = serializer.is_valid(raise_exception=True)
        if not is_valid:
            return Response({'code': 0, 'msg': '失败', 'data': serializer.errors})
        serializer.save()
        # 4,返回响应
        return Response({'code': 1, 'msg': '成功', 'data': serializer.data})


from django.shortcuts import render
# Create your views here.
import time
from django.http import JsonResponse
from rest_framework.views import APIView
class Login(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'code': 1, 'msg': None}
        # 参数是datadict 形式
        id = request.data.get('id')
        pas = request.data.get('password')
        # usr = request._request.POST.get('username')
        # pas = request._request.POST.get('password')
        # usr = request.POST.get('username')
        # pas = request.POST.get('password')
        print(id)
        print(pas)
        # obj = models.User.objects.filter(username='yang', password='123456').first()
        obj = User.objects.filter(id=id, password=pas).first()

        print(type(id))
        if not obj:
            ret['code'] = '0'
            ret['msg'] = '用户名或者密码错误'
            return JsonResponse(ret)
            # 里为了简单，应该是进行加密，再加上其他参数
        token = str(time.time()) + id
        md5 = hashlib.md5()
        md5.update(token.encode())
        token = md5.hexdigest()
        ret['msg'] = '登录成功'
        ret['token'] = token
        data={}
        ret['data'] = data
        data['id'] = obj.id
        data['username'] = obj.username
        data['password'] = obj.password
        data['email']= obj.email
        data['targetCollege'] = obj.targetCollege
        data['targetScore'] = obj.targetScore
        data['currentScore'] = obj.currentScore
        # ret['token'] = token

        return JsonResponse(ret)