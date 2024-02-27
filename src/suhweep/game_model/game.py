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
    def is_valid_cell(self, c: Cell):
        if (c.r < 0) or (c.c < 0):
            return False

        if (c.r >= self.rows):
            return False

        if (c.c >= self.cols):
            return False

        return True

    # ---------------------------------
    def calculate_adj_numbers(self):

        for c in self.cells:
            adj_theoretical_cells = []
            adj_valid_cells = []
            adj_theoretical_cells.append(Cell(c.r + 1, c.c))  # below (S)
            adj_theoretical_cells.append(Cell(c.r + 1, c.c + 1))  # SE
            adj_theoretical_cells.append(Cell(c.r + 1, c.c - 1))  # SW
            adj_theoretical_cells.append(Cell(c.r - 1, c.c))  # above (N)
            adj_theoretical_cells.append(Cell(c.r - 1, c.c + 1))  # NE
            adj_theoretical_cells.append(Cell(c.r - 1, c.c - 1))  # NW
            adj_theoretical_cells.append(Cell(c.r, c.c - 1))  # W
            adj_theoretical_cells.append(Cell(c.r, c.c + 1))  # E

            for tc in adj_theoretical_cells:
                if self.is_valid_cell(tc):
                    adj_valid_cells.append(tc)

            # ---
            nearby_mines = 0
            for vac in adj_valid_cells:
                if CELL_MINE == self.grid[vac.r][vac.c]:
                    nearby_mines += 1

            # ---
            if (nearby_mines > 0) and (CELL_MINE != self.grid[c.r][c.c]):
                self.grid[c.r][c.c] = nearby_mines

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

        # return mines
        return indices + "\n\n" + mines  # + "\n\n" + cells


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    gg = GameGrid(8, 12, 12)

    print(str(gg))
    gg.clear_and_remine()
    print(str(gg))
    gg.calculate_adj_numbers()
    print(str(gg))
    # gg.clear_and_remine()
    # print(str(gg))
