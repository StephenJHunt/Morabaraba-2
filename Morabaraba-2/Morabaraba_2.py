import Morabaraba_OO

game = Morabaraba_OO.MorabarabaGame()

for k, v in game.board.state.items():
    print(f"{k}: {v.state}")