import random

userWins = 0
computerWins = 0

moves = ["rock", "paper", "scissors"] #string in list

while True:
    userMove = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if userMove == "q":
        break
    
    if userMove not in moves:
        continue

    randomNum = random.randint(0, 2) #0 rock, 1 paper, 3 scissors
    computerMove = moves[randomNum]
    print("The computer has picked", computerMove + ".")

    if userMove == "rock" and computerMove == "scissors":
        print("You won!")
        userWins += 1
    elif userMove == "paper" and computerMove == "rock":
        print("You won!")
        userWins += 1
    elif userMove == "scissors" and computerMove == "paper":
        print("You won!")
        userWins += 1
    elif userMove == computerMove:
        print("It's a tie!")
    else:
        print("You lost :(")
        computerWins += 1

print("Your wins:", userWins)
print("Computer wins:", computerWins)
print("gg :D")