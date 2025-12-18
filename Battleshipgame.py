"""
python program for simplified battleshipgame with following rules

game is played in square grid
each player 1 and player 2 or compuuter hides a ship 
each ship occupy exactly threee consec blocks , horizontal or vertical
players cannot overlap ship or place outside grid
players take turn firing shots at opponents grid
if a shot hits part of ship mark as as "X"
if antire shp is discover turn all x into "s"
if shot is a miss mark as "O"
IF player hits  they continue till they miss
the firat player to sink all opponents 3 ships win

"""
import random

GRID_SIZE = int(input("Enter Grid Size: "))
SHIP_LENGTH = 3
TOTAL_SHIPS = 3
choice = input("Enter your Choice (P or C): ").upper()

def create_grid():
    return [["~"] * GRID_SIZE for _ in range(GRID_SIZE)]

def print_grid(grid, hide=True):
    print("  ", end="")
    for i in range(GRID_SIZE):
        print(i, end=" ")
    print()
    for i in range(GRID_SIZE):
        print(i, end=" ")
        for j in range(GRID_SIZE):
            if hide and grid[i][j] == "S":
                print("~", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()
    print()

def player_place_ships(grid):
    ships = []
    while len(ships) < TOTAL_SHIPS:
        print_grid(grid, hide=False)

        try:
            pos, orient = input(f"Ship {len(ships)+1}: ").split()
            r, c = map(int, pos.split(","))
            orient = orient.upper()
        except:
            print_grid(grid, hide=False)
            continue


        ship = []
        for i in range(SHIP_LENGTH):
            nr = r + (i if orient == "V" else 0)
            nc = c + (i if orient == "H" else 0)
            if nr < 0 or nc < 0 or nr >= GRID_SIZE or nc >= GRID_SIZE or grid[nr][nc] == "S":
                ship = []
                break
            ship.append((nr, nc))

        if ship:
            for x, y in ship:
                grid[x][y] = "S"
            ships.append(ship)
        
    print_grid(grid, hide=False)
    
    return ships

def computer_place_ships(grid):
    ships = []
    while len(ships) < TOTAL_SHIPS:
        ship = []
        orient = random.choice(["H", "V"])
        r, c = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        for i in range(SHIP_LENGTH):
            nr = r + (i if orient == "V" else 0)
            nc = c + (i if orient == "H" else 0)
            if nr >= GRID_SIZE or nc >= GRID_SIZE or grid[nr][nc] == "S":
                ship = []
                break
            ship.append((nr, nc))
        if ship:
            for x, y in ship:
                grid[x][y] = "S"
            ships.append(ship)
    return ships

def ship_sunk(ship, grid):
    for r, c in ship:
        if grid[r][c] != "X":
            return False
    return True

def fire(grid, ships, r, c):
    if r < 0 or c < 0 or r >= GRID_SIZE or c >= GRID_SIZE:
        return True

    if grid[r][c] == "~":
        grid[r][c] = "O"
        return False

    if grid[r][c] == "S":
        grid[r][c] = "X"
        for ship in ships:
            if (r, c) in ship and ship_sunk(ship, grid):
                print("Ship sunk!")
        return True

    return True

def all_ships_sunk(ships, grid):
    return all(ship_sunk(ship, grid) for ship in ships)

player_grid = create_grid()
computer_grid = create_grid()

if choice == "C":
    player_ships = player_place_ships(player_grid)
    computer_ships = computer_place_ships(computer_grid)

    while True:
        print("Your Turn")
        print_grid(computer_grid)

        while True:
            r, c = map(int, input("Fire (row col): ").split())
            if fire(computer_grid, computer_ships, r, c):
                print("HIT")
                print("player")
                print_grid(computer_grid)
                print("computer")
                print_grid(player_grid)
                if all_ships_sunk(computer_ships, computer_grid):
                    print("player")
                    print_grid(computer_grid)
                    print("computer")
                    print_grid(player_grid)
                    print("YOU WIN")
                    exit()
            else:
                print("Miss")
                print("player")
                print_grid(computer_grid)
                print("computer")
                print_grid(player_grid)
                break

        print("Computer Turn")
        while True:
            r, c = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if player_grid[r][c] in ["X", "O"]:
                continue
            if fire(player_grid, player_ships, r, c):
                print("HIT")
                print("player")
                print_grid(computer_grid)
                print("computer")
                print_grid(player_grid)
                if all_ships_sunk(player_ships, player_grid):
                    print("player")
                    print_grid(computer_grid)
                    print("computer")
                    print_grid(player_grid)
                    print("COMPUTER WINS")
                    exit()
            else:
                print("MISS")
                print("player")
                print_grid(computer_grid)
                print("computer")
                print_grid(player_grid)
                break

elif choice == "P":
    print("PLAYER 1 SHIPS")
    player_ships = player_place_ships(player_grid)
    print("PLAYER 2 SHIPS")
    computer_ships = player_place_ships(computer_grid)

    while True:
        print("Player 1 Turn")
        while True:
            r, c = map(int, input("Fire (row col): ").split())
            if fire(computer_grid, computer_ships, r, c):
                print("Hit")
                print("player1")
                print_grid(computer_grid)
                print("player2")
                print_grid(player_grid)
                if all_ships_sunk(computer_ships, computer_grid):
                    print("player1")
                    print_grid(computer_grid)
                    print("player2")
                    print_grid(player_grid)
                    print("PLAYER 1 WINS")
                    exit()
            else:
                print("Miss")
                print("player1")
                print_grid(computer_grid)
                print("player2")
                print_grid(player_grid)
                break

        print("Player 2 Turn")
        while True:
            r, c = map(int, input("Fire (row col): ").split())
            if fire(player_grid, player_ships, r, c):
                print("HIT")
                print("player1")
                print_grid(computer_grid)
                print("player2")
                print_grid(player_grid)

                if all_ships_sunk(player_ships, player_grid):
                    print("player1")
                    print_grid(computer_grid)
                    print("player2")
                    print_grid(player_grid)
                    print("PLAYER 2 WINS")
                    exit()
            else:
                print("Miss")
                print("player1")
                print_grid(computer_grid)
                print("player2")
                print_grid(player_grid)
                break
