from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from tictactoe.models import Game


@login_required
def home(request):
    template_name = 'user_account/home.html'
    # my_games = Game.objects.games_for_user(request.user)
    my_games = Game.objects.filter(
        Q(first_player=request.user) | Q(second_player=request.user))
    active_games = my_games.filter(status="A")
    finished_games = my_games.exclude(status="A")
    waiting_games = active_games.filter(next_to_move=request.user)
    other_games = active_games.exclude(next_to_move=request.user)
    return render(request, template_name, locals())
