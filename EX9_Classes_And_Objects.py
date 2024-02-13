# This exercise is aimed at practicing classes and objects by building a Sudoku Solver 

# the instantiation of a class creates an empty object. Classes can have methods that acre like local functions for each instance

# the __init__ method is a special method that allows to instantiate an object to a customized state. When a class implements an __init__ method, __init__ is automatically called upon instantiation 
# __init__ takes the parameter "self": this is a reference to the instance of the class

# create a class for the board 
class Board: 
    def __init__(self, board):
        # self.board refers to the board attribute of the instance of the class. It's a variable that belongs to the object created from the Board class
        self.board = board

    def __str__(self):
        # create the board lines 
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'

        board_string = upper_lines

# Enumeration is a convenient way to keep track of both the element and its position on a list. The enumerate() function is a built-in function in Python that takes an iterable (such as a list, tuple, or string) and returns an iterator that produces tuples containing indices and corresponding values from the iterable.
        
        for index, line in enumerate(self.board):
            
            # store the elements of a single row in the sudoku board
            row_list = []
            
            # split each row in three segments in order to represent the 3x3 squares properly
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start = 1):
                
                # join the elements of the segment(part) with a pipe character                
                # access all elements
                row_square = '|'.join(str(item) for item in part)
                
                # Extend the row_list with the elements of the row_square string
                row_list.extend(row_square) 

                # check if the current segment (square_no) is not the last one
                if square_no != 3:
                    row_list.append('║')

        # create a string representation of the row with spaces between each element
        row = f'║ {" ".join(row_list)} ║\n' 

        # replace the 0 that will be used for empty cells with a space
        row_empty = row.replace('0', ' ')

        # board_string is gradually built up as the loop iterates over each row, creating the full ASCII art representation of the sudoku board
        board_string += row_empty

        # check if the row index is 8, as it will be handled differently:
        if index < 8:
            
            # verify if the row is the last row inside a 3x3 square
            if index % 3 == 2:
                
                # in order to create a visually appealing border, append a different border string to board_string 
                board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
            
            # if the inner condition is False, the current row is not the last row of a 3x3 square 
            else:
                board_string += middle_lines

        # handle the last row of the entire board 
        else: 
            board_string += lower_lines
    
        # after the outer loop completes for all rows, return the string that contains the complete visual representation of the sudoku board
        return board_string
    
    # method that finds the empty cells in the sudoku board
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            
            # attempt to find the index of the first occurrence of 0 in the current row
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass

        # if the loop completes without finding any empty cells, the method should return None to indicate that the sudoku board is filled
        return None
    
    # method that checks if a given number can be inserted into a specified row of the sudoku board
    # self: representing the instance of the class
    # row: row index
    # num: the number to be checked 
    def valid_in_row(self, row, num):
        
        # check if the number is not already present in that row
        return num not in self.board[row]
    
    # method that checks if a number can be inserted in a specified column of the sudoku board by checking if the number is not already present in that column for any row 
    def valid_in_col(self, col, num):

        # generate a list of boolean values representing whether the condition is True for each element in the specified column across all rows
        return all(
            
            # for each element in the specified column (col) of the current row (row), check whether the value at the current position in the 2D list is not equal to the provided num
            self.board[row][col] != num

            # check if a given number is not equal to the number in the specified column of the current row
            for row in range(9)
        )
    
    # check if a number can be inserted in the 3x3 square
    # row: row index 
    # col: column index 
    # num: number to be checked
    def valid_in_square(self, row, col, num):
        
        # calculate the starting row index for the 3x3 block in the board grid
        row_start = (row // 3) * 3

        # calculate the starting column index for the 3x3 block in the board grid
        col_start = (col // 3) * 3

        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        
        # if the number is not present, it can be inserted into the square without violating the rules of sudoku
        return True
    
    # check if a given number is a valid choice for an empty cell in the sudoku board by validating its compatibility with the row, column, and 3x3 square of the specified empty cell
    # empty: a tuple representing the row and column indices of an empty cell 
    # num: number to be checked
    def is_valid(self, empty, num):

        # unpack the "empty" tulip inro the row and column values
        row, col = empty 

        # check if the number is valid for insertion in the specified row
        valid_in_row = self.valid_in_row(row, num)

        # check if the number is valid for insertion in the specified column 
        valid_in_col = self.valid_in_col(col, num)

        # check if the number is valid for insertion in the 3x3 square that contains the specified cell
        valid_in_square = self.valid_in_square(row, col, num)

        # verify that all the function calls return True and return the result
        return all([valid_in_row, valid_in_col, valid_in_square])
    
    # method that attempts to solve the sudoku in-place (modify the existing sudoku board rather than creating a new one)
    def solver(self):
        
        # check if there are any empty cells left in the sudoku board. By using the walrus operator (:=), combine the assignment and the conditional check into a single line, making the code more concise and readable
        if (next_empty := self.find_empty_cell()) is None:

            # if there are no empty cells (i.e., next_empty is None), the puzzle is solved. So, return True
            return True
        
        # the case where there are empty cells and the puzzle is unsolved
        else: 
            for guess in range(1, 10):

                # for each number (guess), check if the number is a valid choice for the current empty cell
                if self.is_valid(next_empty, guess):

                    # if the guess is valid, the method updates the sudoku board with the guess by assigning guess to the cell specified by "next_empty"
                    row, col = next_empty

                    # access the cell at the given row and column in the sudoku board
                    self.board[row][col] = guess 

                    # recursively call self.solver() to try to solve the rest of the sudoku
                    self.solver()

                    # if the recursive call to self.solver() returns True, it means the sudoku is solved
                    if self.solver():
                        return True
            
                    # if self.solver() returns False, this means the "guess" led to an unsolvable sudoku. So, reset the guess to 0
                    self.board[row][col] = 0

            # return False when none of the guesses leads to a solution 
            return False
        
# function to print and solve the sudoku board
def solve_sudoku(board):

    # create a board
    gameboard = Board(board)

    # print the board
    print(f'\nPuzzle to solve:\n{gameboard}')

    # check if the solver() method call from the gameboard object returns True. If so, pring the solved puzzle
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)

    # print the message if the puzzle is unsolvable
    else:
        print('\nThe provided puzzle is unsolvable.')

    # return teh instance of the Board class, which represents the final state of the sudoku board after attempting to solve it
    return gameboard 

# test run: 
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

solve_sudoku(puzzle)