class MorabarabaGame:
    class Board:
        class Cell:
            def __init__(self, state):
                self.state = state

        def __init__(self):
            #initialise state
            self.state = {"A1": " ", "A4": " ", "A7": " ",
                          "B2": " ", "B4": " ", "B6": " ",
                          "C3": " ", "C4": " ", "C5": " ",
                          "D1": " ", "D2": " ", "D3": " ",
                          "D5": " ", "D6": " ", "D7": " ",
                          "E3": " ", "E4": " ", "E5": " ",
                          "F2": " ", "F4": " ", "F6": " ",
                          "G1": " ", "G4": " ", "G7": " "}
            #relationships for neighbours
            self.neighbours = {"A1": ['D1', 'A4', 'B2'], "A4": ['A1', 'B4', 'A7'], "A7": ['A4', 'B6', 'D7'],
                               "B2": ['A1', 'D2', 'C3', 'B4'], "B4": ['B2', 'A4', 'C4', 'B6'], "B6": ['B4', 'C5', 'D6', 'A7'],
                               "C3": ['B2', 'C4', 'D3'], "C4": ['C3', 'B4', 'C5'], "C5": ['C4', 'D5', 'B6'],
                               "D1": ['A1', 'G1', 'D2'], "D2": ['D1', 'F2', 'D3', 'B2'], "D3": ['D2', 'E3', 'C3'],
                               "D5": ['E5', 'D6', 'C5'], "D6": ['D5', 'F6', 'D7', 'B6'], "D7": ['D6', 'G7', 'A7'],
                               "E3": ['F2', 'E4', 'D3'], "E4": ['E3', 'F4', 'E5'], "E5": ['E4', 'F6', 'D5'],
                               "F2": ['G1', 'F4', 'E3', 'D2'], "F4": ['F2', 'G4', 'F6', 'E4'], "F6": ['F4', 'G7', 'D6', 'E5'],
                               "G1": ['D1', 'G4', 'F2'], "G4": ['G1', 'F4', 'G7'], "G7": ['G4', 'F6', 'D7']}
            #mills
            self.mills = [['A1','A4','A7'], ['B2','B4','B6'], ['C3','C4','C5'], ['D1','D2','D3'], ['D5','D6','D7'],
                          ['E3','E4','E5'], ['F2','F4','F6'], ['G1','G4','G7'], ['A1','D1','G1'], ['B2','D2','F2'],
                          ['C3','D3','E3'], ['A4','B4','C4'], ['E4','F4','G4'], ['C5','D5','E5'], ['B6','D6','F6'],
                          ['A7','D7','G7'], ['A1','B2','C3'], ['A7','B6','C5'], ['G1','F2','E3'], ['G7','F6','E5']]
    board = Board()
    xstones, ostones = 12, 12

    def displayBoard(self):
        a1 = self.board.state['A1']
        a4 = self.board.state['A4']
        a7 = self.board.state['A7']
        b2 = self.board.state['B2']
        b4 = self.board.state['B4']
        b6 = self.board.state['B6']
        c3 = self.board.state['C3']
        c4 = self.board.state['C4']
        c5 = self.board.state['C5']
        d1 = self.board.state['D1']
        d2 = self.board.state['D2']
        d3 = self.board.state['D3']
        d5 = self.board.state['D5']
        d6 = self.board.state['D6']
        d7 = self.board.state['D7']
        e3 = self.board.state['E3']
        e4 = self.board.state['E4']
        e5 = self.board.state['E5']
        f2 = self.board.state['F2']
        f4 = self.board.state['F4']
        f6 = self.board.state['F6']
        g1 = self.board.state['G1']
        g4 = self.board.state['G4']
        g7 = self.board.state['G7']
        #if your IDE is as silly as mine, this next assignment will be underlined in
        #a very silly and annoying red, but still compile.
        #ignore the silly Microsoft red.
        display = f''' 
player X: {self.xstones} player O: {self.ostones}
    1   2  3   4   5  6   7      
A   {a1}----------{a4}----------{a7}   
|   | '.       |        .'|      
B   |   {b2}------{b4}------{b6}   |   
|   |   |'.    |    .'|   |      
C   |   |  {c3}---{c4}---{c5}  |   |   
|   |   |  |       |  |   |      
D   {d1}---{d2}--{d3}       {d5}--{d6}---{d7}
|   |   |  |       |  |   |      
E   |   |  {e3}---{e4}---{e5}  |   |   
|   |   |.'    |    '.|   |      
F   |   {f2}------{f4}------{f6}   |   
|   |.'        |       '. |      
G   {g1}----------{g4}----------{g7}            
                  '''
        print('\n'*100)
        print(display)






    def getOpponent(self, player):
        if player == "X":
            return "O"
        return "X"

    def getInputPos(self, prompt):
        while (True):
            inpt = (input(prompt + ": ")).upper()
            if inpt in self.board.state.keys():
                break
            print("Invalid input, try again")
        return inpt   

    def inMill(self, pos):
        for mill in self.board.mills:
            if pos in mill:
                if self.board.state[mill[0]] != " " and (self.board.state[mill[0]] == self.board.state[mill[1]] == self.board.state[mill[2]]):
                    return True
        return False

    def allInMill(self, player):
        for key, state in self.board.state.items():
            if state == player and not self.inMill(key):
                return False
        return True

    def shootCow(self, player):
        self.displayBoard()
        while(True):
            pos = self.getInputPos("Choose cow to shoot")
            if self.board.state[pos] != player and self.board.state[pos] != " ":
                if not self.inMill(pos) or self.allInMill(self.getOpponent(player)):
                    self.board.state[pos] = " "
                    break
            else:
                self.displayBoard()
                print("Please only shoot your opponent's cows that aren't in a mill")
    
    def runPlacingPhase(self):
        def placePiece(player):
            self.displayBoard()
            while(True):
                pos = self.getInputPos("Choose position to place")
                if self.board.state[pos] != " ":
                    self.displayBoard()
                    print("Please place a piece on an empty position")
                else:
                    self.board.state[pos] = player
                    if self.inMill(pos): self.shootCow(player)
                    break
    
        player = "X"
        while (self.ostones > 0 and self.xstones > 0):
            placePiece(player)
            if player == "X":
                self.xstones -= 1
                player = "O"
            else:
                self.ostones -= 1
                player = "X"
    def runMovingPhase(self):
        def getAdjacentSquares(pos):
            return self.board.neighbours[pos]
        def movePiece(pos):
            return None
        
    def runGame(self):
        runPlacingPhase()
        runMovingPhase()

