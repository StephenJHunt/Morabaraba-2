class MorabarabaGame:
    class Board:
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


    def runGame(self):
        def displayBoard():
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


        def getOpponent(player):
            if player == "X":
                return "O"
            return "X"

        def getInputPos(prompt):
            while (True):
                inpt = (input(prompt + ": ")).upper()
                if inpt in self.board.state.keys():
                    break
                displayBoard()
                print("Invalid input, try again")
            return inpt   

        def inMill(pos):
            for mill in self.board.mills:
                if pos in mill:
                    if self.board.state[mill[0]] != " " and (self.board.state[mill[0]] == self.board.state[mill[1]] == self.board.state[mill[2]]):
                        return True
            return False

        def allInMill(player):
            for key, state in self.board.state.items():
                if state == player and not inMill(key):
                    return False
            return True

        def shootCow(player):
            displayBoard()
            while(True):
                pos = getInputPos("Choose cow to shoot")
                if self.board.state[pos] != player and self.board.state[pos] != " ":
                    if not inMill(pos) or allInMill(getOpponent(player)):
                        self.board.state[pos] = " "
                        break
                displayBoard()
                print("Please only shoot your opponent's cows that aren't in a mill")
        
        def runPlacingPhase():
            def placePiece(player):
                displayBoard()
                while(True):
                    pos = getInputPos("Choose position to place")
                    if self.board.state[pos] != " ":
                        displayBoard()
                        print("Please place a piece on an empty position")
                    else:
                        self.board.state[pos] = player
                        if inMill(pos): shootCow(player)
                        break
        
            player = "X"
            while (self.ostones > 0 or self.xstones > 0):
                placePiece(player)
                if player == "X":
                    self.xstones -= 1
                    player = "O"
                else:
                    self.ostones -= 1
                    player = "X"
        def runMovingPhase():
            def getPlayerCount(player):
                return len(list(filter(lambda state: state == player, self.board.state.values())))
            xcount = getPlayerCount("X")
            ocount = getPlayerCount("O")
            player = "X"
            def getAdjacentSquares(pos):
                return self.board.neighbours[pos]
            def pieceMovable(pos):
                neighbours = getAdjacentSquares(pos)
                for neighbour in neighbours:
                    if self.board.state[neighbour] == " ":
                        return True
                return False
            def selectPiece():
                displayBoard()
                while True:
                    pos = getInputPos("Select a cow to move")
                    if (player == "X" and xcount == 3) or (player == "O" and ocount == 3):
                        moveFlyingPiece(pos)
                        break
                    if pieceMovable(pos): 
                        if self.board.state[pos] == player:
                            moveNormalPiece(pos)
                            break
                    displayBoard()
                    print("Please select a valid cow to move")
            def moveFlyingPiece(takePos):
                displayBoard()
                while True:
                    pos = getInputPos('move {} to'.format(takePos))
                    if self.board.state[pos] == " ":
                        self.board.state[takePos] = " "
                        self.board.state[pos] = player
                        if inMill(pos): shootCow(player)
                        break
                    displayBoard()
                    print("Please place piece on an empty square")
            def moveNormalPiece(takePos):
                displayBoard()
                while True:
                    pos = getInputPos('move {} to'.format(takePos))
                    if pos in getAdjacentSquares(takePos) and self.board.state[pos] == " ":
                        self.board.state[takePos] = " "
                        self.board.state[pos] = player
                        if inMill(pos): shootCow(player)
                        break
                    displayBoard()
                    print("Please place piece on an adjacent empty square")
            def canPlay():
                for pos, state in self.board.state.items():
                    if state == player and pieceMovable(pos):
                        return True
                return False
                        
            #########################################################
            #########################################################
            displayBoard()
            if ocount == xcount == 12:
                print("DRAW!!!")
                return
            while (xcount > 2 and ocount > 2):
                if not canPlay():
                    print(getOpponent(player) + " won!")
                selectPiece()
                if player == "X":
                    player = "O"
                    ocount = getPlayerCount("O")
                else:
                    player = "X"
                    xcount = getPlayerCount("X")

            if xcount > 3:
                print("O won!")
            else:
                print("X won!")
        runPlacingPhase()
        displayBoard()
        runMovingPhase()

