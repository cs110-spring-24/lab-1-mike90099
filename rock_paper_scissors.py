#1 == rock
#2 == paper
#3 == scissors
#
#
import random
cpu = random.randint(1,3)
user =input("Enter rock, paper, or scissors:")

if user == "rock":
	if cpu == 1:  #cpu chose rock
		print("Tie game because the computer chose rock as well!")
	elif cpu == 2: # cpu chose paper
		print("Unfortunately, you lost since the computer chose paper.")
	else: #cpu chose scissors
		print("You win because the computer chose scissors!")	
if user == "paper":		
	if cpu == 2:  #cpu chose paper
		print("Tie game because the computer chose paper as well!")
	elif cpu == 3: # cpu chose scissors
		print("Unfortunately, you lost because the computer chose scissors.")
	else: #cpu chose rock
		print("You win because the computer chose rock!")
if user == "scissors":		
	if cpu == 3:  #cpu chose scissors
		print("Tie game because the computer chose scissors as well!")
	elif cpu == 1: # cpu chose rock
		print("Unfortunately, you lost because the computer chose rock.")
	else: #cpu chose scissors
		print("You win because the computer chose paper!")
