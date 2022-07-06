# -*- coding: utf-8 -*-
from enum import Enum

# NOTE: DRY. Lets have the texts a little centralized
class IndividualPoints(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    DEUCE = 4

    @classmethod
    def _missing_(cls, value: object):
        return IndividualPoints.DEUCE




# NOTE: Fragment the current code to be more organized and prevent issues
#  in the long run. Keep the hoofs on the horse, don't put them on the cat
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.points = 0

    def get_name(self) -> str:
        return self.name

    def add_point(self) -> None:
        self.points += 1

    def set_points(self, points: int) -> None:
        self.points = points

    def get_points(self) -> str:
        return self.points

    def get_points_enum(self) -> IndividualPoints:
        return IndividualPoints(self.points)

    def get_points_display(self) -> str:
        return IndividualPoints(self.points).name.title()

    def __str__(self) -> str:
        return f'{self.name} - {self.points}'


class Game:
    # NOTE: Lets think about paired games later
    # def __init__(self, players: list):
    #     self.players = [Player(p) for p in players]

    def __init__(self, player1: str, player2: str):
        self.players = [
            Player(player1),
            Player(player2),
        ]

    def add_point(self, playerName: str):
        for p in self.players:
            if playerName == p.get_name():
                p.add_point()
                break

    def get_score_display(self) -> str:
        player1 = self.players[0]
        player2 = self.players[1]

        # Same amount points
        if (player1.get_points() == player2.get_points()):
            # Print only DEUCE
            if (player1.get_points_enum() in [IndividualPoints.FORTY, IndividualPoints.DEUCE]):
                return player1.get_points_display()
            # Print that it is a tie
            return f'{player1.get_points_display()}-All'

        # Maybe someone already won
        if (player1.get_points_enum() in [IndividualPoints.FORTY, IndividualPoints.DEUCE]):
            abovePlayer = max(player1, player2, key = lambda p: p.get_points())
            belowPlayer = min(player1, player2, key = lambda p: p.get_points())

            # Someone has the advantage
            if abs(abovePlayer.get_points() - belowPlayer.get_points()) == 1:
                return f'Advantage {abovePlayer.get_name()}'

            # Someone already won
            if abovePlayer.get_points() >= 4 and abs(abovePlayer.get_points() - belowPlayer.get_points()) >= 2:
                return f'Win for {abovePlayer.get_name()}'

        return f'{player1.get_points_display()}-{player2.get_points_display()}'

    def won_point(self, playerName: str) -> None:
        self.add_point(playerName)

    def score(self) -> str:
        return self.get_score_display()
