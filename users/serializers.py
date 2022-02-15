'''
定义序列化器
1,定义类,继承自Serializer
2,和模型类,字段名字一样
3,和模型类,字段类型一样
4,和模型类,字段选项一样

反序列化
    校验
        1,字段类型校验
        2,字段选项校验
        3,单字段校验,方法
        4,多字段
        5自定义
'''
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ["id","username","email"]
        extra_kwargs = {
            "password":{
                "max_length":11,
                "min_length": 5,
            }

        }

    # 单字段校验
    def validate_email(self,value):
        if "@" not  in value:
            raise serializers.ValidationError("请输入正确邮箱格式")
        return value


