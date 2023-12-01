import random
from pprint import pprint


scores = {
    "computer_score" : 0,
    "player_score" : 0
}
grid_size = 5

def g_size():
    """
    set the grid(board) size
    """
    while True:
        print("Please set your grid(board) size.")
    
        data = input("Enter a number here:\n")
        validate_g_size(data)

        if validate_g_size(data):
            print("Number is valid!")
            break

    return data   

def validate_g_size(value):
    """
    Validate user input to set the grid(board) size
    """
    try:
        grid_type =[4,5]
        value = int(value)
        if value not in grid_type :
            raise ValueError(
                f"Number 4 or 5 is required, you provided {value}"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def new_game():
    """
    Starts the game with board populated, while setting both computer and player score to zero
    
    """

    print("-----------------------------------") 
    print( "Welcome to our BATTLESHIPS GAME!")
    print("-----------------------------------")
    grid_size = g_size()
    print( "Number of ships: 4")
    print(f"Grid size(board): {grid_size}")
    print("-----------------------------------")


new_game()