import os
import json
import random
from dataclasses import dataclass

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------ constants
# 0.8 means you cant have 8 mines if you have 10 cells total. you would need 7 or less.
MAX_MINE_FRACTION = 0.8

CELL_CLEAR = '-'
CELL_MINE = '*'


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(frozen=True)
class Cell:
    r: int = None
    c: int = None

    def __str__(self):
        return f"<{self.r}, {self.c}>"


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
class GameGrid:

    def __init__(self, rows, cols, mine_count):
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count

        max_number_of_mines_allowed = int(rows * cols * MAX_MINE_FRACTION)
        if mine_count >= max_number_of_mines_allowed:
            raise Exception(f"Too many mines. Cant place {mine_count} mines in {rows} x {cols} grid.")

        self.grid = []
        self.cells = []

        for r in range(rows):
            curr_row = []
            self.grid.append(curr_row)
            for c in range(cols):
                curr_row.append(CELL_CLEAR)
                self.cells.append(Cell(r, c))

    # ---------------------------------
    def clear_and_remine(self):
        """ Clear grid and randomly place mines in the grid. """

        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = CELL_CLEAR

        tmp_mc = self.mine_count
        while tmp_mc > 0:
            cell = random.choice(self.cells)
            if CELL_CLEAR == self.grid[cell.r][cell.c]:
                self.grid[cell.r][cell.c] = CELL_MINE
                tmp_mc -= 1

    # ---------------------------------
    def __str__(self) -> str:
        mines = ""
        indices = ""

        for r in range(self.rows):
            for c in range(self.cols):
                indices += f"<{r}, {c}>   "
                mines += f"<{self.grid[r][c]}>   "
            # ---
            indices += "\n"
            mines += "\n"
            cells = " ".join([str(c) for c in self.cells])

        return mines
        # return indices + "\n\n" + mines  # + "\n\n" + cells

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    gg = GameGrid(8, 12, 12)

    print(str(gg))
    gg.clear_and_remine()
    print(str(gg))
    gg.clear_and_remine()
    print(str(gg))
