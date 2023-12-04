from pydantic import BaseModel


class Player(BaseModel):
    name: str
    buildings: list
    shields: list
    atk: list
    alive: bool


class GameRoom(BaseModel):
    players: list = list()
    player_turn: int = 0
    game_turn: int = 0
    # timer: int = 0
    max_players: int = 2
    started: bool


class Action(BaseModel):
    action: str
    body: any
