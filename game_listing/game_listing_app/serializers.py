from rest_framework import serializers
from .models import Game

class GameListSerialzer(serializers.ModelSerializer):
    """
    Serializer for Game model
    """
    title = serializers.ReadOnlyField()
    platform = serializers.ReadOnlyField()
    score = serializers.ReadOnlyField()
    genre = serializers.ReadOnlyField()
    editors_choice = serializers.ReadOnlyField()

    class Meta:
        model = Game
        fields = '__all__'