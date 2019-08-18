from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from . import serializers
from .models import Game


def response(data, code=status.HTTP_200_OK, error=None):
    """
    Overrides rest_framework response
    :param data: data to be send in response
    :param code: response status code(default has been set to 200)
    :param error: error message(if any, not compulsory)
    """
    return Response(data=data, status=code)


def get_all_game_list():
    """
    return list of all games
    :param request:
    :param status:
    :return:
    """
    all_game = Game.objects.all()
    serializer = serializers.GameListSerialzer(all_game, many=True)
    return response(serializer.data)


def get_game_by_title(title):
    games = Game.objects.filter(title__contains=title)
    if games.exists():
        serializer = serializers.GameListSerialzer(games, many=True)
        return response(serializer.data)
    else:
        raise APIException(detail='No game contains this title')
