import cfbd
from config import api_client

games_api = cfbd.GamesApi(api_client)
stats_api = cfbd.StatsApi(api_client)


def get_games(team, year):
    return games_api.get_games(year=year, team=team)


def get_stats(team, year):
    return stats_api.get_player_season_stats(year=year, team=team)