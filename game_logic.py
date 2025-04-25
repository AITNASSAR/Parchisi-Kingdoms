import random

class AIPlayer:
    def __init__(self, name):
        self.name = name; self.score = 0

    def make_move(self, game_state):
        return random.choice(game_state["available_moves"])

class Game:
    def __init__(self, players):
        self.players = players
        self.board = [None]*100
        self.current_player_index = 0

    def next_turn(self):
        self.current_player_index = (self.current_player_index+1)%len(self.players)
        cp = self.players[self.current_player_index]
        if isinstance(cp, AIPlayer):
            move = cp.make_move({"available_moves":[i for i,c in enumerate(self.board) if c is None]})
            self.update_board(move, cp)

    def update_board(self, move, player):
        self.board[move] = player.name
        player.score += 1
