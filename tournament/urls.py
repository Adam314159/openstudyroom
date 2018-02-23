from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<tournament_id>[0-9]+)/$',
        views.tournament_view,
        name='view'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/games/$',
        views.games,
        name='games'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/players/$',
        views.players,
        name='players'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/games/(?P<sgf_id>[0-9]+)$',
        views.games,
        name='games'
    ),
    url(
        r'^create/$',
        views.TournamentCreate.as_view(success_url='/tournament/list/'),
        name='create'
    ),
    url(
        r'^list/$',
        views.tournament_list,
        name='list'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/settings/$',
        views.manage_settings,
        name='manage_settings'
    ),

    url(
        r'^(?P<tournament_id>[0-9]+)/groups/$',
        views.manage_groups,
        name='manage_groups'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/brackets/$',
        views.manage_brackets,
        name='manage_brackets'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/manage_games/$',
        views.manage_games,
        name='manage_games'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/upload_sgf/$',
        views.upload_sgf,
        name='upload_sgf'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/create-sgf/$',
        views.create_sgf,
        name='create_sgf'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/set-stage/$',
        views.set_stage,
        name='set_stage'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/invite/$',
        views.invite_user,
        name='invite_user'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/quit/$',
        views.remove_players,
        name='remove_players'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/save_players_order/$',
        views.save_players_order,
        name='save_players_order'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/create-group/$',
        views.create_group,
        name='create_group'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/create-bracket/$',
        views.create_bracket,
        name='create_bracket'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/save-groups/$',
        views.save_groups,
        name='save_groups'
    ),
    url(
        r'^create-match/(?P<round_id>[0-9]+)/$',
        views.create_match,
        name='create_match'
    ),
    url(
        r'^delete_match/(?P<round_id>[0-9]+)/$',
        views.delete_match,
        name='delete_match'
    ),
    url(
        r'^create-round/(?P<bracket_id>[0-9]+)/$',
        views.create_round,
        name='create_round'
    ),
    url(
        r'^rename-round/(?P<round_id>[0-9]+)/$',
        views.rename_round,
        name='rename_round'
    ),
    url(
        r'^delete-round/(?P<round_id>[0-9]+)/$',
        views.delete_round,
        name='delete_round'
    ),
    url(
        r'^(?P<tournament_id>[0-9]+)/save-brackets/$',
        views.save_brackets,
        name='save_brackets'
    ),
    url(
        r'^rename-bracket/(?P<bracket_id>[0-9]+)/$',
        views.rename_bracket,
        name='rename_bracket'
    ),
    url(
        r'^delete-bracket/(?P<bracket_id>[0-9]+)/$',
        views.delete_bracket,
        name='delete_bracket'
    ),

]