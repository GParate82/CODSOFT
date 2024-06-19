import random 

print ("\n                             .......Welcome to Rock Paper Scissors Game.......\n")
print("                                  ................Lets Start................")

cpuScore = 0
playerScore = 0
tieScore = 0
possibleHands = ["Rock", "Paper", "Scissors"]

def checkForWinner(playerHand, computerHand):
    if (playerHand == "Rock" and computerHand == "Paper"):
        print ("Sorry you lost...!!!\n")
        return "Cpu"

    elif (playerHand == "Rock" and computerHand == "Scissors"):
        print("Congratulations...You won.!!!!!\n")
        return "Player"

    elif (playerHand == "Scissors" and computerHand == "Paper"):
        print("Congratulations...You won.!!!!!\n")
        return "Player"

    elif (playerHand == "Scissors" and computerHand == "Rock"):
        print("Sorry you lost...!!!\n")
        return "Cpu"

    elif (playerHand == "Paper" and computerHand == "Rock"):
        print("Congratulations...You won.!!!!!\n")
        return "Player"

    elif (playerHand == "Paper" and computerHand == "scissors"):
        print("Sorry you lost...!!!\n")
        return "Cpu"
        
    else:
        print("It is a tie, play again!\n")
        return "Tie"
    
while (playerScore != 3 and cpuScore != 3):
    while True:
        playerHand = input("\nPick a hand, Rock, Paper or Scissors: ")
        if(playerHand == "Rock" or playerHand == "Paper" or playerHand == "Scissors"):
            break
        else:
            print("\nInvalid input...Try again...")

    ##Generate computer pick
    computerHand = random.choice(possibleHands)

    ###Print results
    print("\nYour hand: ", playerHand)
    print("Cpu hand: ", computerHand)
    result = checkForWinner(playerHand, computerHand)
    if(result == "Player"):
        playerScore += 1
    elif(result == "Cpu"):
        cpuScore += 1
    else:
        tieScore += 1
    print("Your Score:",playerScore,", Cpu:",cpuScore, ", Ties:",tieScore)

print ("\n Game Over...!!! Thank you for playing...!!!\n")