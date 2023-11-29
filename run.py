import random
from pprint import pprint


scores = {
    "computer_score" : 0,
    "player_score" : 0
}


grid_size = 5
#print( " Number of ships: 4")
#print("-----------------------------------")

   
def new_game():
    """
    Starts the game with board populated, while setting both computer and player score to zero
    
    """

    print("-----------------------------------") 
    print( " Welcome to our BATTLESHIPS GAME!")
    print("-----------------------------------")

size = input("Please enter board size e.g it must be 4 or 5 \n")
grid_size = size
print(f"size is {grid_size}")

new_game()