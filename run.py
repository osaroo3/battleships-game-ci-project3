import random
from pprint import pprint


scores = {
    "computer_score" : 0,
    "player_score" : 0
}
grid_size = 5

player_ship_coordinate = []
player_guess_coordinate = []

comp_ship_coordinate = []
comp_guess_coordinate = []


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

def ran_row(size):
    """
    Random number between 1 and size-1
    """
    return random.randint(1,size-1)


def ran_col(size):
    """
    Random number between 0 and size-1
    """
    return random.randint(0,size-1)


def add_ships(board,ships):
    """
    """
    for t in range(ships):
        x = ran_row(ships)
        y = ran_col(ships)
        player_ship_coordinate.append((x,y))
        board[x][y] = "@"


def game_board(board,ships): 
    """
    """
    add_ships(board,ships)
    pprint(board)
    for r in board:
        g = (" ".join(r))
        print(g)
    return(g)


def new_game():
    """
    Starts the game with board populated, while setting both computer and player score to zero
    
    """

    print("-----------------------------------") 
    print( "Welcome to our BATTLESHIPS GAME!")
    print("-----------------------------------")
    grid_size = int(g_size())
    #print( "Number of ships: 4")
    print(f"Grid size(board): {grid_size}")
    num_ships = 4
    print(f"Number of ships : {num_ships}")
    print("-----------------------------------")

    # Game board without ships
    g_board = [["." for i in range(grid_size)] for j in range(grid_size)]

    print("-----------------------------------")   
    name = input("Enter your name here:\n")
    print(f"{name}'s board")
    game_board(g_board, num_ships)


new_game()