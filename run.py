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
        grid_type =[5,6]
        value = int(value)
        if value not in grid_type :
            raise ValueError(
                f"Number 5 or 6 is required, you provided {value}"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def ran_one(size):
    """
    Random number between 1 and size-1
    """
    return random.randint(1,size-1)


def ran_two(size):
    """
    Random number between 0 and size-1
    """
    return random.randint(0,size-1)


def add_ships(board,ships,player_type="player"):
    """
    Add ships to board
    """
    if player_type != "player":
        for n in range(ships):
            a = ran_one(ships)
            b = ran_one(ships)
            board[a][b] = "#"
            comp_ship_coordinate.append((a,b))
    else:
        for n in range(ships):
            x = ran_two(ships)
            y = ran_two(ships)
            board[x][y] = "@"
            player_ship_coordinate.append((x,y))
            
       


def game_board(board,ships,player_type=""): 
    """
    Prints board(player or computer) with ships appended
    """
    add_ships(board,ships,player_type)
    #pprint(board)
    for r in board:
        g = (" ".join(r))
        print(g)
    return(g)


def player_turn(board,turn):
    row = int(input("Enter a row : \n")) 
    column =  int(input("Enter a column : \n")) 
    print(f"You entered row:{row} column:{column}") 

    if (row,column) not in comp_ship_coordinate:
        print("You missed!")
        player_guess_coordinate.append((row,column))
        print(player_guess_coordinate)
        board[row][column] = "X"

    else:
        print("You hit!")
        player_guess_coordinate.append((row,column))
        print(player_guess_coordinate)
        board[row][column] = "*"
        scores["player_score"] += 1

        if scores["player_score"] == 1:
            print("Player wins!")

   
def turns(board, turn=""):
    """
    Handles both player and computer turns
    """
    if turn != "player_turn":
        comp_turn(board, "computer_turn")
    else:
        player_turn(board, "player_turn")    

def new_game():
    """
    Starts the game with board populated, while setting both computer and player score to zero
    
    """

    print("-----------------------------------") 
    print( "Welcome to our BATTLESHIPS GAME!")
    print("-----------------------------------")
    grid_size = int(g_size())
    print(f"Grid size(board): {grid_size}")
    num_ships = 4
    print(f"Number of ships : {num_ships}")
    print("-----------------------------------")

    # Game board without ships
    player_board = [["." for i in range(grid_size)] for j in range(grid_size)]
    computer_board = [["." for i in range(grid_size)] for j in range(grid_size)]
    
    print("-----------------------------------")   
    name = input("Enter your name here:\n")
    print(f"{name}'s board")
    game_board(player_board, num_ships,"player")
    print(player_ship_coordinate)
    print(" ")
    print(f"Computer's board")
    game_board(computer_board, num_ships,"computer")
    print(comp_ship_coordinate)


    turns(player_board, "player_turn")

new_game()