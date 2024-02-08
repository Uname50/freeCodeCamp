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
