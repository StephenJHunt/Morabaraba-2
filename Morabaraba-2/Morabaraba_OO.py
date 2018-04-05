class MorabarabaGame:
    class Board:
        class Cell:
            def __init__(self, state):
                self.state = state

        def __init__(self):
            #initialise state
            self.state = {"A1": self.Cell("Empty"), "A4": self.Cell("Empty"), "A7": self.Cell("Empty"),
                          "B2": self.Cell("Empty"), "B4": self.Cell("Empty"), "B6": self.Cell("Empty"),
                          "C3": self.Cell("Empty"), "C4": self.Cell("Empty"), "C5": self.Cell("Empty"),
                          "D1": self.Cell("Empty"), "D2": self.Cell("Empty"), "D3": self.Cell("Empty"),
                          "D5": self.Cell("Empty"), "D6": self.Cell("Empty"), "D7": self.Cell("Empty"),
                          "E3": self.Cell("Empty"), "E4": self.Cell("Empty"), "E5": self.Cell("Empty"),
                          "F2": self.Cell("Empty"), "F4": self.Cell("Empty"), "F6": self.Cell("Empty"),
                          "G1": self.Cell("Empty"), "G4": self.Cell("Empty"), "G7": self.Cell("Empty")}
            #relationships for neighbours
            self.neighbours = {"A1": ['D1', 'A4', 'B2'], "A4": ['A1', 'B4', 'A7'], "A7": ['A4', 'B6', 'D7'],
                               "B2": ['A1', 'D2', 'C3', 'B4'], "B4": ['B2', 'A4', 'C4', 'B6'], "B6": ['B4', 'C5', 'D6', 'A7'],
                               "C3": ['B2', 'C4', 'D3'], "C4": ['C3', 'B4', 'C5'], "C5": ['C4', 'D5', 'B6'],
                               "D1": ['A1', 'G1', 'D2'], "D2": ['D1', 'F2', 'D3', 'B2'], "D3": ['D2', 'E3', 'C3'],
                               "D5": ['E5', 'D6', 'C5'], "D6": ['D5', 'F6', 'D7', 'B6'], "D7": ['D6', 'G7', 'A7'],
                               "E3": ['F2', 'E4', 'D3'], "E4": ['E3', 'F4', 'E5'], "E5": ['E4', 'F6', 'D5'],
                               "F2": ['G1', 'F4', 'E3', 'D2'], "F4": ['F2', 'G4', 'F6', 'E4'], "F6": ['F4', 'G7', 'D6', 'E5'],
                               "G1": ['D1', 'G4', 'F2'], "G4": ['G1', 'F4', 'G7'], "G7": ['G4', 'F6', 'D7']}
    board = Board()
    
    def shootCow(pos):
        return None
    def inMill(pos):
        return None
    def checkMills():
        return None

    def getInputPos(self):
        while (True):
            inpt = input("Enter a position: ")
            if inpt.upper() in self.board.state.keys():
                break
            print("Invalid input, try again")
        return inpt
    
    def runPlacingPhase():
        def placePiece():
            return None

    def runMovingPhase(self):
        def getAdjacentSquares(pos):
            return self.board.neighbours[pos]
        def movePiece(pos):
            return None
        
    def runGame(self):
        runPlacingPhase()
        runMovingPhase()

