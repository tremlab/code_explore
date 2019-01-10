import sudoku
import unittest


class testSudoku(unittest.TestCase):

    # def test_grid4_equals_2(self):
    #     row = "3.5.7.924"
    #     self.assertEqual(sudoku.find_row_options(row), set([1, 6, 8]))

    def setUp(self):
        values_str = "4..36.2955..1..64.....5...1..8.314.....5.9.....574.3..6...2.....83..4..7149.75..3"
        global board
        board = sudoku.build_sudoku_board(values_str)

    def test_board_build(self):
        """to confirm the board is built correctly.
        """
        last_cell = None
        for c in board.cells_settled:
            if c.row == 9 and c.column == 9:
                last_cell = c

        self.assertEqual(last_cell.value, 3)

    def test_eval_board_false(self):
        """starting board is NOT solved.
        """
        self.assertEqual(board.evaluate_board(), False)

    def test_eval_board_true(self):
        """artificially setting up the 'win' scenario - no open squares.
        """
        board.cells_settled = board.cells_settled.union(board.cells_open)
        board.cells_open = set([])
        self.assertEqual(board.evaluate_board(), True)

    def tearDown(self):
        global board
        board = None

if __name__ == '__main__':
    unittest.main()
