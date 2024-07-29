letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


# mapping letters to points using zip (creates a tuple) and put inside a dict.
letters_to_points = {letter:point for letter,point in zip(letters, points)}

# adding blank tiles
letters_to_points[' '] = 0


# func that will take in word and return word value(points)
def score_word(word):
    point_total = 0
    for letter in word.upper():
        if letter in letters_to_points.keys():
            point = letters_to_points.get(letter, 0)
            point_total += point  
    return point_total


# should be 25 points!!!
pizza_points = score_word("pizza")

# dict that maps different players to words they have already played
players_to_words = {
    'Player1000': {'Red', 'Football', 'Oreo'},
    'wordExpert': {'Fart', 'Eyes', 'Toner'},
    'NoCheater': {'Taco', 'Super', 'Juiced'},
    'Mr.Mrs': {'Crap', 'Water', 'Games'}
    }

players_to_points = {}
# iterating through items(player,words) and totaling point value for each player, mappin this in dict.
for player, words in players_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    players_to_points[player] = player_points


print(f'This shows Letter Value {letters_to_points}')
print(f'This is a sample player game {players_to_words}')
print(f'This maps players to points {players_to_points}')



