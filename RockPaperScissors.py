import random

def play_game():
    player = False
    cpu_score = 0
    player_score = 0
    while True:
        player = input("Rock, Paper or Scissors?").capitalize()
        choices = ["Rock", "Paper", "Scissors"]
        computer = random.choice(choices)
        ## Conditions of Rock, Paper and Scissors
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
                cpu_score += 1
            else:
                print("You win!", player, "smashes", computer)
                player_score += 1
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
                cpu_score += 1
            else:
                print("You win!", player, "covers", computer)
                player_score += 1
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose...", computer, "smashes", player)
                cpu_score += 1
            else:
                print("You win!", player, "cut", computer)
                player_score += 1
        elif player == 'End':
            print("Final Scores:")
            print(f"CPU:{cpu_score}")
            print(f"Player:{player_score}")
            break

if __name__ == "__main__":
    #play_game()
    from CC import showgraph
    from Hal import showHalsteadGraph

    showgraph("RockPaperScissors.py")
    showHalsteadGraph("RockPaperScissors.py")


