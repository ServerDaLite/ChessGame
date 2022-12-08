"""
R N B K Q B N R
P P P P P P P P
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
P P P P P P P P
R N B K Q B N R
"""



class Chess():
    def __init__(self):
        self.board = self.generateBoard()
    
    def generateBoard(self):
        return [["#"for i in range(8)] for i in range(8)]
        
    def displayBoard(self):
        print("\n".join([" ".join(i) for i in self.board]))
        
    def setPiece(self, piece, position):
        self.board[len(self.board)-position[1]-1][position[0]] = piece
     
if __name__ == "__main__":
    game = Chess()
    
    # BLACKS
    game.setPiece("R", (0, 0))
    game.setPiece("N", (1, 0))
    game.setPiece("B", (2, 0))
    game.setPiece("K", (3, 0))
    game.setPiece("Q", (4, 0))
    game.setPiece("B", (5, 0))
    game.setPiece("N", (6, 0))
    game.setPiece("R", (7, 0))
    
    game.setPiece("P", (0, 1))
    game.setPiece("P", (1, 1))
    game.setPiece("P", (2, 1))
    game.setPiece("P", (3, 1))
    game.setPiece("P", (4, 1))
    game.setPiece("P", (5, 1))
    game.setPiece("P", (6, 1))
    game.setPiece("P", (7, 1))
    
    # WHITES
    game.setPiece("R", (0, 7))
    game.setPiece("N", (1, 7))
    game.setPiece("B", (2, 7))
    game.setPiece("K", (3, 7))
    game.setPiece("Q", (4, 7))
    game.setPiece("B", (5, 7))
    game.setPiece("N", (6, 7))
    game.setPiece("R", (7, 7))
    
    game.setPiece("P", (0, 6))
    game.setPiece("P", (1, 6))
    game.setPiece("P", (2, 6))
    game.setPiece("P", (3, 6))
    game.setPiece("P", (4, 6))
    game.setPiece("P", (5, 6))
    game.setPiece("P", (6, 6))
    game.setPiece("P", (7, 6))
    
    game.displayBoard()


### END OF FILE ###
