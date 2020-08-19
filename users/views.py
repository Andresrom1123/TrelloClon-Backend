from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from users.serializers import UserSerializer
from tableros.models import Tabled
from tableros.serializers import TabledSerializer, CreateTabledSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un usuario de acuerdo al ID mandado.
    list:
        Regresa la lista de usuario en la base de datos.
    create:
        Crea un usuario en la base de datos.
    delete:
        Elimina un usuario.
    update:
        Actualiza un libro.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['GET'])
    def tableros(self, request, pk=None):
        """
        Regresa los tableros de un usuario.
        """
        # /users/1/tableros
        dueno = self.get_object()  # => users.objects.get(id=1)
        tableros = Tabled.objects.filter(dueno__id=dueno.id)
        serialized = TabledSerializer(tableros, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def tablerosfavoritos(self, request, pk=None):
        """
        Regresa los tableros favoritos de un usuario.
        """
        # /users/1/tablerosfavoritos
        favorite = self.get_object()  # => users.objects.get(id=1)
        tableros = Tabled.objects.filter(favorite__id=favorite.id)
        serialized = TabledSerializer(tableros, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
