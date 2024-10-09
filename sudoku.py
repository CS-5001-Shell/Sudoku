from boards import *


def read_board(filename: str) -> list[list[int]]:
    """Reads a file containing a 9x9 sudoku
    board formated as nine rows of nine
    comma-separated integers. Creates a list
    containing nine lists where each list
    is a row of the text file.
    Parameter:
      filename (str) is the location of the file.
    Return:
      a list of lists representing the board
    Raises:
     FileNotFoundError if location is not found
     ValueError if file format is invalid
    Example file text:
    0,5,0,0,1,0,0,4,0
    1,0,1,0,0,0,6,0,2
    0,0,0,9,0,5,0,0,0
    2,0,8,0,3,0,5,0,1
    0,4,0,0,7,0,0,2,0
    9,0,1,0,8,0,4,0,6
    0,0,0,4,0,1,0,0,0
    3,0,4,0,0,0,7,0,9
    0,2,0,0,6,0,0,1,0
    Expected data structure:
            [
                [0,5,0,0,1,0,0,4,0],
                [1,0,1,0,0,0,6,0,2],
                [0,0,0,9,0,5,0,0,0],
                [2,0,8,0,3,0,5,0,1],
                [0,4,0,0,7,0,0,2,0],
                [9,0,1,0,8,0,4,0,6],
                [0,0,0,4,0,1,0,0,0],
                [3,0,4,0,0,0,7,0,9],
                [0,2,0,0,6,0,0,1,0]
            ]

    """
    pass


def check_rows(board: list[list[int]]) -> bool:
    """Returns True if every row in the board
    data structure contains all numbers 1-9
    and False otherwise.
    """
    pass


def check_columns(board: list[list[int]]) -> bool:
    """Returns True if every column in the board
    data structure contains all numbers 1-9
    and False otherwise.
    """
    pass


def check_squares(board: list[list[int]]) -> bool:
    """Returns True if every subsquare in the board
    data structure contains all numbers 1-9
    and False otherwise.
    """
    pass


def candidate_values(board: list[list[int]],
                     row: int,
                     column: int) -> list[int]:
    """Determines all candidate values for a given
    square.
    Parameters:
      board (list[list[lint]])
      row (int) represents the row
      column (int) represents the column
    Return:
      list[int] all possible integers that can
       go in the given square.
    This function does not "look ahead". It will
    return a list of the numbers that do not appear
    in the row specified by row, nor the column
    specified by column, nor the subsquare in
    which the square is located.
    """
    pass


def solve(board: list[list[int]]) -> bool:
    """Returns True if the board can be solved
    and False if not.
    If the board can be solved then the board
    data structure will contain the solution
    when the function completes. If the board
    cannot be solved then the board will have
    all of the original data after the function
    completes.

    Parameter:
      board (list[list[int]])
    Return:
      bool
    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()
