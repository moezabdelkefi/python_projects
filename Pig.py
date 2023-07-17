import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("enter the numbers of players (2-4): ")
    # convert string to integer
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("must be between 1 - 4 players")

    else:
        print("invalis, must be a number.")

# store each players scores in the array
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nplayer number", player_idx + 1, "turn has just started!")
        print("your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("you rolled a 1! turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a:", value)
                print("your score is:", current_score)

        player_scores[player_idx] += current_score
        print("your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player", winning_idx + 1, "is the winner with a score of:", max_score)
