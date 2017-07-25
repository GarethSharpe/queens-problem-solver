'''
Created on July 4, 2017

@author: Gareth Sharpe
'''

class Board():
    '''
    classdocs
    '''

    def __init__(self, size):
        '''
        Constructor
        '''
        self._width, self._height = size, size
        self._board = [[0 for _ in range(self._width)] for _ in range(self._height)] 
        self._size = 65;
        self._sep = '-' * (4 * size + 1)
    
    def __str__(self):
        letter = 'A'
        '''
        Prints the Chess board
        '''
        i = self._width - 1
        string = "  " + self._sep
        for row in self._board: # @UnusedVariable
            string += "\n" + str(i + 1) + ' |'
            for col in self._board:
                if col[i] == 0 or col[i] == 1:
                    string += '   |'
                else:
                    string += ' ' + str(col[i]) + ' |'
            i -= 1
            string += '\n  ' + self._sep
        i = self._width
        string += "\n    "
        while i > 0:
            string += letter
            string += '   '
            i -= 1
            letter = chr(ord(letter) + 1)
        string += "\n"
        return string
    
    def check_west(self, col, row):
        ''' 
        Checks for attack vectors West of desired placement
        '''
        safe = True
        while safe and col >= 0:
            if not isinstance(self._board[col][row], Queen):
                col -= 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row + 1))
                safe = False
        
        return safe
    
    def check_east(self, col, row):
        ''' 
        Checks for attack vectors East of desired placement
        '''
        safe = True
        while safe and row < (self._width - 1):
            if not isinstance(self._board[col][row], Queen):
                    row += 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row + 1))
                safe = False
        
        return safe
    
    def check_north(self, col, row):
        ''' 
        Checks for attack vectors North of desired placement
        '''
        safe = True
        while safe and row < (self._width - 1):
            if not isinstance(self._board[col][row], Queen):
                    row += 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row + 1))
                safe = False
        
        return safe

    def check_south(self, col, row):
        ''' 
        Checks for attack vectors West of desired placement
        '''
        safe = True
        while safe and row >= 0:
            if not isinstance(self._board[col][row], Queen):
                    row -= 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row - 1))
                safe = False
        
        return safe
    
    def check_north_east(self, col, row):
        ''' 
        Checks for attack vectors North-East of desired placement
        '''
        safe = True
        while safe and row < (self._width) and col < (self._height):
            if not isinstance(self._board[col][row], Queen):
                col += 1
                row += 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row + 1))
                safe = False
        
        return safe
        
    def check_north_west(self, col, row):
        ''' 
        Checks for attack vectors North-West of desired placement
        '''
        safe = True
        while safe and row < (self._width) and col >= 0:
            if not isinstance(self._board[col][row], Queen):
                col -= 1
                row += 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row + 1))
                safe = False
        
        return safe
        
    def check_south_east(self, col, row):
        ''' 
        Checks for attack vectors South-East of desired placement
        '''
        safe = True
        while safe and row >= 0 and col < (self._height):
            if not isinstance(self._board[col][row], Queen):
                col += 1
                row -= 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row + 1))
                safe = False
        
        return safe
        
    def check_south_west(self, col, row):
        ''' 
        Checks for attack vectors South-West of desired placement
        '''
        safe = True
        while safe and row >= 0 and col >= 0:
            if not isinstance(self._board[col][row], Queen):
                col -= 1
                row -= 1
            else:
                # print("Queen at " + chr(col + 65).upper() + str(row + 1))
                safe = False
        
        return safe
    
    
    def check_open(self, col, row):
        return not isinstance(self._board[col][row], Queen)

    def check_safe(self, col, row):
        safe = False
        if self.check_north(col, row):
            if self.check_south(col, row):
                    if self.check_west(col, row):
                            if self.check_north_west(col, row):
                                    if self.check_south_west(col, row):
                                        safe = True
        return safe
        
    def place_queen(self, queen, pos):
        '''
        Attempts to place queen at given row, col vector
        '''
        col = ord(pos[0]) - 65
        row = int(pos[1]) - 1
        placed = False
        safe = False
        
        # print("Placing Queen at " + pos, end='.\n')
        
        open = self.check_open(col, row) # @ReservedAssignment
        
        # print("Open: " + str(open))

        if open:
            safe = self.check_safe(col, row)
            # print("Safe:", str(safe))
        
        if open and safe:
            self._board[col][row] = queen
            placed = True
        
        return placed
    
    def solve(self, col=0):
        solved = False
        n = self._width - 1
        i = 0
        
        if col == (n+1):
            print(self)
            return
        
        if not solved:
            while i <= n:
                if self.check_safe(col, i):
                    q = Queen()
                    c = chr(col + 65)
                    pos = c + str(i + 1)
                    self.place_queen(q, pos)
                    solved = self.solve(col + 1)
                    self._board[col][i] = 0
                i += 1
        
        return solved
        
class Queen():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def __str__(self):
        return 'Q'   
