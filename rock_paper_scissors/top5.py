import csv

players_scores = {}
file = open('score.csv', 'r')
file.readline()

for line in file:
    row = line.strip().split(',')
    username = row[0]
    user_score = row[2]
    if username in players_scores:
        players_scores[username] += user_score
    else:
        players_scores[username] = user_score

file.close
sorted_players = sorted(players_scores.items(), key=lambda x: x[1] )
top_players = []
for i in range(min(5, len(sorted_players))):  
    top_players.append(sorted_players[i])
print("Top 5 Players:")
for i, (player, score) in enumerate(top_players, start=1):
    print(f"{i}. {player} - Total Score {score}")
                                