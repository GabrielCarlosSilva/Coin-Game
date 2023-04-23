import random
import os

turns=0
maxTurns=5
player_play=" "
cpu_play=" "
cpu_points=0
player_points=0
strategy=0
profile=" "
cpu_decision="___"

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
            if player_play=="y":
                board[0]="_O_"
            if player_play=="n":
                board[0]="_X_"
        except:
            print("Try again")

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
    global profile
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

        print("You was playing against the " + profile)

def chooser():
    global turns
    global strategy

    if turns==0:
        strategy=random.randrange(1,4)

def thief():
    global turns
    global maxTurns
    global cpu_decision
    if turns<maxTurns:
        cpu_decision="_X_"
        turns+=1
    else:
        turns+=1

def cooperator():
    global turns
    global maxTurns
    global cpu_decision
    if turns<maxTurns:
        cpu_decision="_O_"
        turns+=1
    else:
        turns+=1  

def chaotic():
    global turns
    global maxTurns
    global cpu_play
    global cpu_decision
    if turns<maxTurns:
        cpu_play=random.randrange(1,5)
        if cpu_play==1:
            cpu_decision="_X_"
            turns+=1
        if cpu_play==2:
            cpu_decision="_O_"
            turns+=1
    else:
        turns+=1

def intermediary():
    global strategy
    global profile
    if strategy==1:
        chaotic()
        profile="Chaotic"
    elif strategy==2:
        thief()
        profile="Thief"
    elif strategy==3 or strategy==4:
        cooperator()
        profile="Cooperator"

def writer():
    global cpu_decision
    board[1]=cpu_decision

while turns<maxTurns:
    chooser()
    intermediary()
    pTurn()
    writer()
    screen()
    result()
    score()