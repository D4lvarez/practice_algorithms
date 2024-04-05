rows: int = 8
columns: int = 8
queens: int = 8
grid: list = []
locked_rows: list = []
locked_columns: list = []

for i in range(rows):
    group = []
    for j in range(columns):
        group.append({f"{i}:{j}": False})
    grid.append(group)

# print(grid)

for cells in grid:
    # cell_locked = None
    # cell_group = None
    for cell in cells:
        for k, v in cell.items():
            if (
                v is False
                and f'{k.split(":")[0]}' not in locked_rows
                and f'{k.split(":")[1]}' not in locked_columns
            ):
                cell[k] = True
                locked_rows.append(k.split(":")[0])
                locked_columns.append(k.split(":")[1])

# print(locked_rows, locked_columns)

# def lock_queen_position(grid: list, locked: list):
#     for dimension in grid:
#         for k, v in dimension.items():
#             if v is False and k not in locked:
#                 for i in dimension
#                 dimension[k] = True
#                 locked.append(k)

#     return grid


# data = lock_queen_position(grid, locked_positions)

# print(data, locked_positions)
