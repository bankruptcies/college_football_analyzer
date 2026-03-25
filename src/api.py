import cfbd
from config import api_client

games_api = cfbd.GamesApi(api_client)
stats_api = cfbd.StatsApi(api_client)

# gets games for year and team, uses API key
def get_games(team, year):
    return games_api.get_games(year=year, team=team)

# gets stats for year and team, uses API key
def get_stats(team, year):
    return stats_api.get_player_season_stats(year=year, team=team)

# gets the years for team called
def get_available_years(team):
    available_years = []

    # checks what years the team has stats for
    # 1860 because CFB was founded in 1869, and 2100 so that it doesnt have to be updated consistently
    for year in range(1860, 2100):  # safe range
        try:
            games = get_games(team, year)

            if games and len(games) > 0:
                available_years.append(year)

        except Exception:
            continue

    return available_years