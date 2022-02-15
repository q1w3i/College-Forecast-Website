from rest_framework import serializers
from college.models import Seventeen,Eighteen,Nineteen,Twenty

class SeventeenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seventeen
        fields = "__all__"

class EighteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eighteen
        fields = "__all__"

class NineteenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nineteen
        fields = "__all__"

class TwentySerializer(serializers.ModelSerializer):
    class Meta:
        model = Twenty
        fields = "__all__"