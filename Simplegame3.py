import random
from time import sleep
#Create user score and computer score initalizers
print("Welcome to the Rock,Paper,Scissors Game - where you will battle against the computer by choosing Rock,Paper, or Scissors!")
print("Once you see 'SHOOT', enter your choice and await the result. Good Luck!")
#Computer chooses random choice between rock,paper, and scissors
user_score = 0
computer_score = 0
def innerlose():
    print("You lose!")
    print("User Score:",user_score)
    print("Computer Score:", computer_score)
    startmessage()
def innerwin():
    print("You win!")
    print("User Score:",user_score)
    print("Computer Score:", computer_score)
    startmessage()
def innertie():
    print("You tied, starting again!")
    print("User Score:",user_score)
    print("Computer Score:", computer_score)
    startmessage()

def startmessage():
    print("Here we go!")
    choices = ['Rock','Paper','Scissors']
    computer_answer = random.choice(choices)
    print("Rock")
    sleep(2)
    print("Paper")
    sleep(2)
    print("Scissors")
    sleep(2)
    
    while True:
        user_answer = input("SHOOT(type 'q' to quit): ")
        if (user_answer.lower() != "rock") and (user_answer.lower() != "paper") and (user_answer.lower() != "scissors") and (user_answer.lower() != "q"):
            print("You must choose between Rock, Paper, or Scissors!")
            continue
        if user_answer == "q":
            quit()

        print("Computer answer: ",computer_answer)
        global user_score
        global computer_score
        if user_answer.lower() == "rock" and computer_answer == "Scissors":
            user_score += 1
            innerwin()
        elif user_answer.lower() == "rock" and computer_answer == "Paper":
            computer_score += 1
            innerlose()
        elif user_answer.lower() == "rock" and computer_answer == "Rock":
            innertie()
        elif user_answer.lower() == "paper" and computer_answer == "Rock":
            user_score += 1
            innerwin()
        elif user_answer.lower() == "paper" and computer_answer == "Scissors":
            computer_score += 1
            innerlose()
        elif user_answer.lower() == "paper" and computer_answer == "Paper":
            innertie()
        elif user_answer.lower() == "scissors" and computer_answer == "Paper":
            user_score += 1
            innerwin()
        elif user_answer.lower() == "scissors" and computer_answer == "Rock":
            computer_score += 1
            innerlose()
        else:
            innertie()

startmessage()
