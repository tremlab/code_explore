def build_sudoku_board(values_str):
    """takes the initial layout of the sudoku board as a STRING.
        Empty squares indicated by "."
        e.g. "47.5.39..." etc.  exactly 81 chars long (9x9)
    """

    board = Board()

    row = 1
    column = 1

    for i in range(1, 82):
        char = values_str[i - 1]

        if char.isdigit():
            cell = Cell(row, column, int(char))
        else:
            cell = Cell(row, column)

        board.insert_cell(cell)

        # tracking row and columns as we go.
        column += 1
        if i % 9 == 0:
            row += 1
            column = 1

    return board


def find_row_options(row):
    """takes in a string representing the row values,
        blank spaces represented by "." Returns set of possible remaining values.
    """
    row_options = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    for char in row:
        if char.isdigit():
            row_options.discard(int(char))

    return row_options


class Board(object):

    def __init__(self):
        self.cells_settled = set([])
        self.cells_open = set([])
        self.is_complete = False

    def insert_cell(self, cell):
        if cell.value:
            self.cells_settled.add(cell)
        else:
            self.cells_open.add(cell)

    def evaluate_board(self):
        """check to see if the board is complete/won.
        """
        if self.cells_open == set([]) and len(self.cells_settled) == 81:
            self.is_complete = True
            return True
        else:
            return False

    def eliminate_known_options(self, cell):
        """eliminates all known values by row, column & box for one cell
            and returns True if this cell is now settled/solved.
        """
        known_cells = self.cells_settled

        for c in known_cells:
            if c.row == cell.row or c.column == cell.column or c.box == cell.box:
                cell.potential_values.discard(c.value)

        if len(cell.potential_values) == 1:
            cell.value = cell.potential_values.pop()
            self.cells_settled.add(cell)
            self.cells_open.discard(cell)
            return True

        return False

    def easy_pass(self):
        """walk through all open squares and eliminate known values.
        """
        keep_trying = False
        for c in self.cells_open:
            fixed_a_cell = self.eliminate_known_options(c)
            if fixed_a_cell:
                keep_trying = True

        board_solved = self.evaluate_board()
        if board_solved:
            keep_trying = False
        # if we solved the whole board, or couldn't find anything to fix, 
        # no need to keep iterating
        return keep_trying

    def solve_board(self):
        found_something = True

        while found_something:
            found_something = self.easy_pass()

        board_solved = self.evaluate_board()

        if not board_solved:
            pass
            # recursive tries


class Cell(object):
    """each square on the sudoku board.
    """
    def __init__(self, row, column, value=None):
        self.value = value
        if value is None:
            self.potential_values = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

        self.row = row
        self.column = column
        self.box = self.assign_box(row, column)

    #class/helper method
    def assign_box(self, row, column):
        box = None
        # refactor??
        if row <= 3:
            if column <= 3:
                box = 1
            elif column <= 6:
                box = 2
            else:
                box = 3
        elif row <= 6:
            if column <= 3:
                box = 4
            elif column <= 6:
                box = 5
            else:
                box = 6
        else:
            if column <= 3:
                box = 7
            elif column <= 6:
                box = 8
            else:
                box = 9

        return box
