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
