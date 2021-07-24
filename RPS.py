import random

cs = 0
ps = 0

while True:
    choices = ["r","s","p"]
    player = None
    computer = random.choice(choices)

    if computer == "s":
        computer = "Scissors"

    elif computer == "r":
     computer = "Rock"

    elif computer == "p":
        computer = "Paper"


    while player not in choices:
        player = input("Rock[r], paper[p] or scissors[s]?: ").lower()

    if player == "s":
     player = "Scissors"

    elif player == "r":
     player = "Rock"

    elif player == "p":
      player = "Paper"

    if player == computer:
            print("You: ",player)
            print("Computer: ",computer)
            print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
                print("You: ", player)
                print("Computer: ", computer)
                print("You lose!")
                cs = cs + 1
        if computer == "Scissors":
            print("Вы: ", player)
            print("Компьютер: ", computer)
            print("Ты выиграл!")
            ps = ps + 1
    elif player == "Scissors":
        if computer == "Paper":
            print("You: ", player)
            print("Computer: ", computer)
            print("You won!")
            ps = ps + 1
        if computer == "Rock":
            print("You: ", player)
            print("Computer: ", computer)
            print("You lose!")
            cs = cs + 1
    elif player == "Paper":
         if computer == "Scissors":
            print("You: ", player)
            print("Computer: ", computer)
            print("You lose!")
            cs = cs + 1
         if computer == "Rock":
            print("Вы: ", player)
            print("Компьютер: ", computer)
            print("Ты выиграл!")
            ps = ps + 1

    print("Your score: ",ps)
    print("Computer score: ",cs)
    play_again = input("Wanna play again? (Y/N): ").lower()

    if play_again != "y":
        break
print("Game over !")
print("Player's score:",ps)
print("Computer score: ",cs)
print("Bye!")