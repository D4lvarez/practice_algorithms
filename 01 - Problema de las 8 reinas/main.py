def is_attacked(row, col):
    """Check if the queen at (row, col) is attacked by any other queen."""
    for r in range(len(BOARD_BOOLEAN)):
        for c in range(len(BOARD_BOOLEAN[r])):
            if BOARD_BOOLEAN[r][c] and (
                r == row or c == col or abs(r - row) == abs(c - col)
            ):
                return True
    return False


def Queens_Placing(Board_Column):
    if Board_Column >= SIZE_OF_BOARD:
        return True
    else:
        Queen_Placed = False
        Board_Row = 0

        while not Queen_Placed and Board_Row < SIZE_OF_BOARD:
            if not is_attacked(Board_Row, Board_Column):
                BOARD_BOOLEAN[Board_Row][Board_Column] = True
                Queen_Placed = Queens_Placing(Board_Column + 1)
                if not Queen_Placed:
                    BOARD_BOOLEAN[Board_Row][Board_Column] = False
                    Board_Row += 1
            else:
                Board_Row += 1

        return Queen_Placed


def Display_Board():
    Count = 0
    for Board_Row in range(len(BOARD_BOOLEAN)):
        for Board_Column in range(len(BOARD_BOOLEAN[Board_Row])):
            if BOARD_BOOLEAN[Board_Row][Board_Column]:
                print(f"|{ 'Q' }| ", end="")
                Count += 1
            else:
                print(f"|{ '.' }| ", end="")
        print()

    print(f"{Count} queens problem is solved, the queens are placed.\n")


# Initialize the BOARD_BOOLEAN 2D array
SIZE_OF_BOARD = 8
BOARD_BOOLEAN = [[False for _ in range(SIZE_OF_BOARD)] for _ in range(SIZE_OF_BOARD)]

# Call the Queens_Placing function to place the queens
Queens_Placing(0)

# Display the final board
Display_Board()
