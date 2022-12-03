from random import sample
from tests import run_star_test, run_unit_test

INPUT_FILEPATH = './input_02.py'

SCORE_MAP = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    OpponentHand.PAPER+PlayerHand.SCISSORS: 6,
    OpponentHand.SCISSORS+PlayerHand.ROCK: 6,
    OpponentHand.ROCK+PlayerHand.PAPER: 6,
    OpponentHand.PAPER+PlayerHand.PAPER: 3,
    OpponentHand.ROCK+PlayerHand.ROCK: 3,
    OpponentHand.SCISSORS+PlayerHand.SCISSORS: 3,
    OpponentHand.SCISSORS+PlayerHand.PAPER: 0,
    OpponentHand.ROCK+PlayerHand.SCISSORS: 0,
    OpponentHand.PAPER+PlayerHand.ROCK: 0,
}

class OpponentHand:
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'

class PlayerHand:
    ROCK = 'X' # 1pt
    PAPER = 'Y' # 2pts
    SCISSORS = 'Z' # 3pts

class Hand:
    def __init__(self, rock=None, paper=None, scissors=None):
        self.rock = rock
        self.paper = paper
        self.scissors = scissors
        self.throw = None

    def throw(self):
        self.throw = sample([self.rock, self.paper, self.scissors])[0]
        return self
    
class GameRound:
    def __init__(self, player=None, opponent=None):
        self.player = player
        self.opponent = opponent

    def throw(self):
        if self.player is None or self.opponent is None:
            print('broken')
            return None
        self.player.throw()
        self.opponent.throw()

    def score(self):
        if self.player is None or self.opponent is None:
            print('broken')
            return None
        elif self.player.throw is None or self.opponent.throw is None:
            print('broken')
            return None
        return SCORE_MAP[self.player.throw] + SCORE_MAP[self.opponent.throw]

    def play(self):
        self.throw()
    
class Game:
    
    def __init__(self, strategy_guide=None, player_hand=None, opponent_hand=None):
        self.strategy_guide = strategy_guide
        self.player_hand = player_hand
        self.opponent_hand = opponent_hand
    
    @property
    def perfect_score(self):
        perfect_score = 0
        for game_round in self.strategy_guide:
            opponent_throw, player_throw = game_round
            perfect_score += SCORE_MAP[player_throw] + SCORE_MAP[f'{opponent_throw}{player_throw}']
        return perfect_score

def parse_input(filepath):
    # 'A Z' -> 'AZ'
    f = open(filepath)
    readlines = f.readlines()
    strategy_guide = []
    for line in readlines:
        line = line.split(' ')
        strategy_guide.append((line[0], line[1].strip()))
    return strategy_guide

strategy_guide = parse_input(INPUT_FILEPATH)
player_hand = Hand(rock=PlayerHand.ROCK, paper=PlayerHand.PAPER, scissors=PlayerHand.SCISSORS)
opponent_hand = Hand(rock=OpponentHand.ROCK, paper=OpponentHand.PAPER, scissors=OpponentHand.SCISSORS)
game = Game(strategy_guide=strategy_guide, player_hand=player_hand, opponent_hand=opponent_hand)

# Test
# solution 1: What would your total score be if everything goes exactly according to your strategy guide?
# attempt 1: 10290, too low
run_star_test(game.perfect_score, 12855)