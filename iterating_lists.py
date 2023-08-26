players_string = "Messi,Neymar,Mbappe,Salah,Dejong,Havertz"
players = players_string.split(",")  # Splitting the string into separate player names

total_character = 0
for player in players:
    total_character += len(player)

average_length = total_character / len(players)
print("Total characters: {}, Average length: {:.2f}".format(total_character, average_length))
