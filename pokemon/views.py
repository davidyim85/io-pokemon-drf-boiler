from .models import Pokemon
from rest_framework import viewsets, permissions
from .serializers import PokemonSerializers

class PokemonViewSet(viewsets.ModelViewSet):
    queryset=Pokemon.objects.all()
    # serializers_class=PokemonSerializers
    serializer_class=PokemonSerializers
    permission_classes=[permissions.AllowAny]


 