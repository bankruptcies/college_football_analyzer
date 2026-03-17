from src.api import get_games, get_stats
from src.analysis import analyze_team
from src.display import display_results, display_leaders

def main():

    # TEAM INPUT
    while True:
        team = input("Enter a team: ").strip()

        if team == "":
            print("Team name cannot be empty. Please try again.")
        else:
            break

    # YEAR INPUT
    while True:
        try:
            year = int(input("Enter a season year: ").strip())
            break
        except ValueError:
            print("Year must be a number. Try again.")

    # API CALL
    try:
        games = get_games(team, year)
        stats = get_stats(team, year)
    except Exception as e:
        print("Error retrieving data from the API.")
        print(e)
        return

    if not games:
        print("No data found for that team/year.")
        return

    wins, losses, avg_points, highest, leaders = analyze_team(games, stats, team)

    results = {
        "wins": wins,
        "losses": losses,
        "avg_points": avg_points,
        "highest_points": highest
    }

    display_results(team, year, results)
    display_leaders(leaders)


if __name__ == "__main__":
    main()