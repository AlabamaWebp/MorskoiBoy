from pydantic import BaseModel


class Ability:
    def __init__(self, name, strongest, type_):
        self.name = name
        self.strongest = strongest
        self.type = type_  # True = atk | False = defence


class Build:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.defence = 0


buildings = list([
    Build("Образование", 8),
    Build("Образование", 8),
    Build("Образование", 8),
    Build("Образование", 8),
    Build("Образование", 8),
    Build("Образование", 8),
    Build("Образование", 8),
    Build("Образование", 8),
])
shields = list([
    Ability("Защита1", 1, False),
    Ability("Защита2", 2, False),
    Ability("Защита3", 3, False),
])
attaks = list([
    Ability("Атака1", 1, True),
    Ability("Атака2", 2, True),
    Ability("Атака3", 3, True),
])


class Player:
    def __init__(self, name):
        self.name = name
        self.buildings = buildings
        self.shields = shields
        self.atk = attaks
        self.alive = True


class GameRoom:
    def __init__(self, max_pl):
        self.players = list()
        self.player_turn = 0
        self.game_turn = 0
        self.timer = 0
        self.max_players = max_pl
        self.started = False


class Action(BaseModel):
    action: str
    body: any


class GameRoomModel:
    players: list
    player_turn: int
    game_turn: int
    timer: int
    max_players: int
    started: bool
