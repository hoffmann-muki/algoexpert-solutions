def tournamentWinner(competitions, results):
    team_to_points = dict()
    for i, [home_team, away_team] in enumerate(competitions):
        if results[i] == 0:
            if away_team in team_to_points:
                team_to_points[away_team] += 3
            else:
                team_to_points[away_team] = 3
            if home_team not in team_to_points:
                team_to_points[home_team] = 0
        else:
            if home_team in team_to_points:
                team_to_points[home_team] += 3
            else:
                team_to_points[home_team] = 3
            if away_team not in team_to_points:
                team_to_points[away_team] = 0
    sorted_results = sorted(team_to_points.items(), key=lambda x: x[1], reverse=True)
    return sorted_results[0][0]
