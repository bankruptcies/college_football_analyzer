# displays the stats for team
def display_results(team, year, stats):

    print("\n--- Team Analysis ---")

    print(f"Team: {team}")
    print(f"Season: {year}")

    print("\nResults:")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    print(f"Average Points: {stats['avg_points']:.2f}")
    print(f"Highest Scoring Game: {stats['highest_points']}")

# displays the leaders of team
def display_leaders(leaders):

    print("\n--- Team Leaders ---")

    print(f"Passing Leader (touchdowns): {leaders['passing'][0]} ({leaders['passing'][1]})")
    print(f"Rushing Leader (yards): {leaders['rushing'][0]} ({leaders['rushing'][1]})")
    print(f"Receiving Leader (yards): {leaders['receiving'][0]} ({leaders['receiving'][1]})")
    print(f"Tackle Leader (total): {leaders['tackles'][0]} ({leaders['tackles'][1]})")
    print(f"Interception Leader: {leaders['interceptions'][0]} ({leaders['interceptions'][1]})")
    print(f"Sack Leader: {leaders['sacks'][0]} ({leaders['sacks'][1]})")