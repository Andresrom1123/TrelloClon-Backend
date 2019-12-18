from rest_framework import serializers
from tableros.models import Tabled
from users.serializers import UserSerializer


class TabledSerializer(serializers.ModelSerializer):
    """
    General purposse Tableros serializer
    """
    dueno = UserSerializer(read_only=True)
    members = UserSerializer(many=True, read_only=True)
    favorite = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Tabled
        fields = ('id', 'name', 'description', 'fecha_hora', 'dueno', 'visibility', 'favorite', 'members')


class CreateTabledSerializer(serializers.ModelSerializer):
    """
    Create table serializer
    """

    class Meta:
        model = Tabled
        fields = ('id', 'name', 'description', 'fecha_hora', 'dueno', 'visibility', 'favorite', 'members')

