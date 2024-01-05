import sys
import enum
import random

# rock = int("1")
# paper = str("2")
# scissors = str("3")
str ("Rock")
str ("Paper")
str ("Scissors")

playerinput = input ("Please enter your option:\nRock\nPaper or\nScissors\n")

player = str(playerinput)

computerchoice = random.choice("Rock Paper Scissors")
computer = str (computerchoice)
# code does not work - check for operators with str data type
if (player == "Rock" and computer == "Scissors"):
    print("You win!")
elif (player == "Paper" and computer == "Rock"):
    print("You win!")
elif (player == "Scissors" and computer == "Paper"):
    Print("You win!")
elif (player == computerchoice):
    Print ("Its a tie!")
else:
    print("python wins")



