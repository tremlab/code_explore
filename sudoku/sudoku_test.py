import sudoku
import unittest


class testSudoku(unittest.TestCase):

    # def test_grid4_equals_2(self):
    #     row = "3.5.7.924"
    #     self.assertEqual(sudoku.find_row_options(row), set([1, 6, 8]))

    def test_board(self):
        """to confirm the board is built correctly.
        """
        values_str = "4..36.2955..1..64.....5...1..8.314.....5.9.....574.3..6...2.....83..4..7149.75..3"
        board = sudoku.build_sudoku_board(values_str)
        last_cell = None
        for c in board.cells_settled:
            if c.row == 9 and c.column == 9:
                last_cell = c

        self.assertEqual(last_cell.value, 3)

if __name__ == '__main__':
    unittest.main()
