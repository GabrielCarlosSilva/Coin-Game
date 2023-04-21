import random
import os

turns=0
maxTurns=5
play=1
player_play=" "
cpu_play=" "
cpu_points=0.0
player_points=0.0

board=["___","___"]

def screen():
    global board
    print("     " + board[0] + "   |   " + board[1])
    print("_______________________")

def pTurn():
    global turns
    global maxTurns
    global player_play
    if turns<maxTurns:
        try:
            player_play=(input("Insert coin?: [y,n]  "))
            os.system('cls')
            if player_play=="y":
                board[0]="_O_"
            if player_play=="n":
                board[0]="_X_"
        except:
            print("Try again")

def cTurn():
    global turns
    global maxTurns
    global cpu_play
    if turns<maxTurns:
        cpu_play=random.randrange(1,3)
        if cpu_play==1:
            board[1]="_X_"
            turns+=1
        if cpu_play==2:
            board[1]="_O_"
            turns+=1
    else:
        turns+=1

def result():
    global turns
    global cpu_points
    global player_points
    
    if board[0]==board[1] and board[0]=="_X_":
        print("Both cheated, nobody won or lost any points")
    elif board[0]==board[1] and board[0]=="_O_":
        print("Both coopereted, both won 2 points")
        cpu_points+=2
        player_points+=2
    elif board[0]!=board[1] and board[0]=="_X_":
        print("You betrayed you oponent, you won 3 points and they lose 1")
        cpu_points-=1
        player_points+=3
    elif board[0]!=board[1] and board[0]=="_O_":
        print("They betrayed you, you lose 1 point and they won 3 points")
        cpu_points+=3
        player_points-=1

def score():
    global turns
    global cpu_points
    global player_points
    if turns==maxTurns:
        print("Your score: ")
        print(player_points)
        print("Their Score: ")
        print(cpu_points)

        if player_points>cpu_points:
            print("You win")
        elif player_points==cpu_points:
            print("Draw")
        elif player_points<cpu_points:
            print("You lose")

while turns<maxTurns:
    pTurn()
    cTurn()
    screen()
    result()
    score()