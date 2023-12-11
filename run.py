import random


scores = {
    "computer_score" : 0,
    "player_score" : 0
}

COMPUTER_SCORE = scores["computer_score"]
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
        grid_type =[6,7,8]
        value = int(value)
        if value not in grid_type :
            raise ValueError(
                f"Number 6,7 or 8 is required, you provided {value}"
            )
        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

def validate_input(coord="row",size=""):
    """
    set inputs coordinates for targerting ships
    """
    while True:
        if coord != "row":
            data = input("Enter a column : \n")
            validate_coordinates(data,size)
            if validate_coordinates(data,size):
                print("Number is valid!")
                break

        else:
            data = input("Enter a row : \n") 
            validate_coordinates(data,size)
            if validate_coordinates(data,size):
                print("Number is valid!")
                break

    return data 


def validate_coordinates(value,size):
    """
    Validates input coordinates to target ships
    """
    try:
        value = int(value)
        value_list = []
        for i in range(size):
            value_list.append(i)
        if value not in value_list:
            raise ValueError(
                f"Number must be 0 or {size-1} , you provided {value}"
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
            a = ran_one(grid_size)
            b = ran_one(grid_size)
            board[a][b] = "#"
            comp_ship_coordinate.append((a,b))
    else:
        for n in range(ships):
            x = ran_two(grid_size)
            y = ran_two(grid_size)
            board[x][y] = "@"
            player_ship_coordinate.append((x,y))
                   

def game_board(board,ships,player_type=""): 
    """
    Prints board(player or computer) with ships appended
    """
    add_ships(board,ships,player_type)
    
    for r in board:
        g = (" ".join(r))
        print(g)


def count_ship_hits(board):
    """This function counts the number of ships hit on a board."""
    count = 0
    for row in board:
        for column in row:
            if column == "*":
                count += 1
    return count


def player_turn(board,turn,size):
    """
    Function handles player turn, appends guesses to player guess list and computer board
    """
    print("\nPlayer's turn")
    row = int(validate_input("row", size))
    column = int(validate_input("column", size))
    print(f"You entered row:{row} column:{column}") 

    if (row,column) not in comp_ship_coordinate:
        print("You missed!")
        player_guess_coordinate.append((row,column))
        board[row][column] = "X"

    else:
        print("You hit!")
        player_guess_coordinate.append((row,column))
        board[row][column] = "*"
        scores["player_score"] = count_ship_hits(board)
        PLAYER_SCORE = scores["player_score"]
        print(f"Player score: {PLAYER_SCORE}")
        
        
def computer_turn(board,turn,size):
    """
    Function handles computer turn, appends guesses to computer guess list and player board
    """
    print("\nComputer's turn")
    row = random.randint(0,size-1)
    column =  random.randint(0,size-1)
    print(f"Computer entered row:{row} column:{column}") 
    if (row,column) not in player_ship_coordinate:
        print("Computer missed!")
        comp_guess_coordinate.append((row,column))
        board[row][column] = "X"
    else:
        print("Computer hit!")
        comp_guess_coordinate.append((row,column))
        board[row][column] = "*"
        scores["computer_score"] = count_ship_hits(board)
        COMPUTER_SCORE = scores["computer_score"]
        print(f"Computer score: {COMPUTER_SCORE}")

  
def turns(board, turn="", size=""):
    """
    Handles both player and computer turns
    """
    if turn != "player_turn":
        computer_turn(board, "computer_turn",size)
    else:
        player_turn(board, "player_turn",size) 


def print_board(board):
    for n in board:
        g_b = (" ".join(n))
        print(g_b)


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


    while True:
        # Player turn
        turns(computer_board, "player_turn", grid_size )
        print("Computer's board")
        print_board(computer_board)
        
        if count_ship_hits(computer_board) == 4:
            print("-----------------------------------") 
            print("Player wins!")
            print("-----------------------------------") 
            break
        # Computer turn
        turns(player_board, "computer_turn", grid_size )
        print("Player's board")
        print_board(player_board)
        
        if count_ship_hits(player_board) == 4:
            print("-----------------------------------") 
            print("Computer wins!")
            print("-----------------------------------") 
            break
        
    print(f"{name}'s board")
    print_board(player_board)
    print(" ")
    print(f"Computer's board")
    print_board(computer_board)
    print("-----------------------------------") 
    print( "THANK YOU FOR PLAYING!")
    print("-----------------------------------")


new_game()