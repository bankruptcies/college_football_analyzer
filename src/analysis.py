def analyze_team(games, stats, team):

    wins = 0
    losses = 0
    points = []
    highest = 0

    for game in games:

        if game.home_points is None or game.away_points is None:
            continue

        if game.home_team == team:
            team_score = game.home_points
            opp_score = game.away_points
        else:
            team_score = game.away_points
            opp_score = game.home_points

        if team_score > opp_score:
            wins += 1
        else:
            losses += 1

        points.append(team_score)

        if team_score > highest:
            highest = team_score

    avg_points = sum(points) / len(points) if points else 0

    stat_totals = {}

    for stat in stats:

        player = stat.player
        stat_type = stat.stat_type
        category = stat.category
        value = float(stat.stat)

        if player not in stat_totals:
            stat_totals[player] = {
                "passing": 0,
                "rushing": 0,
                "receiving": 0,
                "tackles": 0,
                "interceptions": 0,
                "sacks": 0
            }

        if category == "passing" and stat_type == "TD":
            stat_totals[player]["passing"] += value

        if category == "rushing" and stat_type == "YDS":
            stat_totals[player]["rushing"] += value

        if category == "receiving" and stat_type == "YDS":
            stat_totals[player]["receiving"] += value

        if category == "defensive" and stat_type == "TOT":
            stat_totals[player]["tackles"] += value

        if category == "interceptions" and stat_type == "INT":
            stat_totals[player]["interceptions"] += value

        if category == "defensive" and stat_type == "SACKS":
            stat_totals[player]["sacks"] += value

    leaders = {
        "passing": ("", 0),
        "rushing": ("", 0),
        "receiving": ("", 0),
        "tackles": ("", 0),
        "interceptions": ("", 0),
        "sacks": ("", 0)
    }

    for player, values in stat_totals.items():

        if values["passing"] > leaders["passing"][1]:
            leaders["passing"] = (player, values["passing"])

        if values["rushing"] > leaders["rushing"][1]:
            leaders["rushing"] = (player, values["rushing"])

        if values["receiving"] > leaders["receiving"][1]:
            leaders["receiving"] = (player, values["receiving"])

        if values["tackles"] > leaders["tackles"][1]:
            leaders["tackles"] = (player, values["tackles"])

        if values["interceptions"] > leaders["interceptions"][1]:
            leaders["interceptions"] = (player, values["interceptions"])

        if values["sacks"] > leaders["sacks"][1]:
            leaders["sacks"] = (player, values["sacks"])

    return wins, losses, avg_points, highest, leaders