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


    board = Board()
    
    def movePiece(pos):
        return None
    def getAdjacentSquares(pos):
        return None
    def validPos(pos):
        return None
    def shootCow(pos):
        return None
    def inMill(pos):
        return None
    def checkMills():
        return None
    def placingPhase():
        return None
    def movingPhase():
        return None
    def runGame():
        return None