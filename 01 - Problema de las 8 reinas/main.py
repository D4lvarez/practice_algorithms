class EightQueens:
    SIZE_GRID: int = 8
    GRID: list[list[bool]] = []
    EMPTY_PLACE: bool = False
    QUEEN_PLACE: bool = True
    MOVES_NUMBER: int = 4
    QUEENS: int = 0
    horizontal_moves: list[int] = []
    vertical_moves: list[int] = []

    def __init__(self) -> None:

        for _ in range(0, self.SIZE_GRID):
            cells: list[bool] = []

            for __ in range(0, self.SIZE_GRID):
                cells.append(self.EMPTY_PLACE)

            self.GRID.append(cells)

        for move in range(0, self.MOVES_NUMBER):
            self.horizontal_moves.append(move)
            self.vertical_moves.append(move)

        # up Right
        self.horizontal_moves[0] = -1
        self.vertical_moves[0] = 1

        # down left
        self.horizontal_moves[1] = 1
        self.vertical_moves[1] = -1

        # up left
        self.horizontal_moves[2] = -1
        self.vertical_moves[2] = 1

        # down right
        self.horizontal_moves[3] = 1
        self.vertical_moves[3] = 1

    def under_attack(self, row_grid: int, col_grid: int) -> bool:
        is_attacked: bool = False

        # check row
        for col in range(0, self.SIZE_GRID):
            if self.GRID[row_grid][col] is True:
                is_attacked = True

        # check column
        for row in range(0, self.SIZE_GRID):
            if self.GRID[row][col_grid] is True:
                is_attacked = True

        # check diagonal
        for row, col in zip(range(row_grid, -1, -1), range(col_grid, 8)):
            if self.GRID[row][col]:
                is_attacked = True

        for row, col in zip(range(row_grid, 8), range(col_grid, -1, -1)):
            if self.GRID[row][col]:
                is_attacked = True

        for row, col in zip(range(row_grid, -1, -1), range(col_grid, -1, -1)):
            if self.GRID[row][col]:
                is_attacked = True

        for row, col in zip(range(row_grid, 8), range(col_grid, 8)):
            if self.GRID[row][col]:
                is_attacked = True

        return is_attacked

    def remove_queen(self, row_grid: int, col_grid: int) -> None:
        self.GRID[row_grid][col_grid] = self.EMPTY_PLACE
        self.QUEENS -= 1

    def set_queen(self, row_grid: int, col_grid: int) -> None:
        self.GRID[row_grid][col_grid] = self.QUEEN_PLACE
        self.QUEENS += 1

    def queens_placing(self, col_grid: int) -> bool:
        if col_grid >= self.SIZE_GRID:
            return True
        else:
            queen_placed: bool = False
            row_grid: int = 0

            while not queen_placed and row_grid < self.SIZE_GRID:
                if self.under_attack(row_grid, col_grid):
                    row_grid += 1
                else:
                    self.set_queen(row_grid, col_grid)
                    queen_placed = self.queens_placing(col_grid + 1)

                    if not queen_placed:
                        self.remove_queen(row_grid, col_grid)
                        row_grid += 1

            return self.QUEEN_PLACE

    def display_board(self):
        count: int = 0

        for row_grid in range(len(self.GRID)):
            for col_grid in range(len(self.GRID[row_grid])):
                if self.GRID[row_grid][col_grid]:
                    print(f"|{' Q '}| ", end="")
                    count += 1
                else:
                    print(f"|{' X '}| ", end="")
            print()

        print(f"{count} queens problem is solved, the queens are placed.\n")


if __name__ == "__main__":
    eq = EightQueens()
    eq.queens_placing(0)
    eq.display_board()
