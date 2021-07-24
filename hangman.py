import random
words = ["Hello","World","MintTea","Pikachu","Phone","Book","Knife"]



def hangman(word=words[random.randint(0,6)]):
    win = None
    wrong = 0
    stages = ["",
              " _________",
              "|         |",
              "|         0",
              "|        /|\ ",
              "|        / \ ",
              "You lose!"]

    rletters = list(word)
    board = ["_"] * len(word)

    while wrong <  len(stages) -1:
        char = input("Enter the letter: ")  

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print("\n")
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            win = True
            print("You've won! The word was made up: {}".format(word))
            break
             


hangman()
            

