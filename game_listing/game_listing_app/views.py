import pandas as pd
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from . import utils
from . import models
from .permissions import Check_API_KEY_Auth


# Create your views here.
class GameList(APIView):
    permission_classes = (Check_API_KEY_Auth,)
    """
    API to get list of all games with all data
    """
    def get(self, request, *args, **kwargs):
        return utils.get_all_game_list()


class UploadGames(APIView):
    permission_classes = (Check_API_KEY_Auth,)
    """
    API used to upload data to models, Just a Script can be used to get file as upload one
    with little modification
    """
    def get(self, request, *args, **kwargs):
        df = pd.read_csv('/home/kuliza270/Desktop/prod_folder/game_listing/games.csv')
        title = df.title
        platform = df.platform
        score = df.score
        genre = df.genre
        editors_choice = df.editors_choice
        for i in range(len(df)):
            if editors_choice[i] == 'Y':
                choice = True
            else:
                choice = False
            game = models.Game.objects.create(title=title[i], platform=platform[i], score=score[i], genre=genre[i],
                                              editors_choice=choice)
            game.save()
        return utils.response('data uploaded successfully')


class SearchGame(APIView):
    permission_classes = (Check_API_KEY_Auth,)
    """
    API to search game with title idea
    Exact title is not required
    """
    def get(self, request):
        title = request.GET.get('title')
        if not title:
            raise APIException(detail='title in query parameter is not passed')
        return utils.get_game_by_title(title)
