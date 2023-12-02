
class Coord:
    x: int
    y: int


class Player:
    name: str
    buildings: list
    shields: list
    coord_builds: list
    coord_shields: list
    alive: bool


class GameRoom:
    players: list
    player_turn: str
    game_turn: int
    scale: int
    max_players: int
    started: bool


#    A B C D E
# 1 | S ~ ~ C ~ |
# 2 | ~ M ~ ~ ~ |
# 3 | ~ ~ ~ ~ ~ |
# 4 | ~ ~ C ~ ~ |
# 5 | ~ ~ ~ ~ S |
