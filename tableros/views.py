from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tableros.serializers import TabledSerializer, CreateTabledSerializer
from tableros.models import Tabled
from users.serializers import UserSerializer
from users.models import User


class TabledViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Regresa una instancia de un tablero de acuerdo al ID mandado.
    list:
        Regresa la lista de tablero en la base de datos.
    create:
        Crea un tablero en la base de datos.
    delete:
        Elimina un tablero.
    update:
        Actualiza un tablero.
    """
    queryset = Tabled.objects.all()
    serializer_class = TabledSerializer

    def get_serializer_class(self):
        # retrieve
        if self.action == 'create':
            return CreateTabledSerializer
        else:
            return TabledSerializer
        return TabledSerializer

    @action(detail=True, methods=['GET'])
    def dueno(self, request, pk=None):
        """
        Regresa el dueño de un tablero.
        """
        # /tableros/1/dueno
        tableros = self.get_object()  # => tableros.objects.get(id=1)
        dueno = tableros.dueno
        serialized = UserSerializer(dueno)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['POST'])
    def fav(self, request, pk=None):
        """
        Agrega los tableros a favoritos
        """
        # /tableros/id del tablero que quiero agregar a favorito/fav
        tableros = self.get_object()  # => tableros.objects.get(id=1) #Obtengo el tablero del id del usuario
        idusers = request.data.get('users') # Obtengo el id del usuario que mando desde el front
        user = User.objects.get(id=idusers) # Busco el usuario con el id y lo asigno a una variable
        if tableros.favorite.filter(id=user.id).exists(): # Si el usuario ya este como favorito en el tablero
            tableros.favorite.remove(user) # Lo elimino en caso que ya este como favorito
        else:
            tableros.favorite.add(user) # Sino esta lo agrego
        tableros.save() # Guardo el usuario del tablero
        return Response(status=status.HTTP_200_OK)
