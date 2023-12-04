from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from Data.core import GameRoom, Action

# from Data.core import

app = FastAPI()


class ConnectionManager:
    def __init__(self, max_pl, pl):
        self.max_players = max_pl
        self.players = pl
        self.active_connections: list[WebSocket] = []

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def connect(self, websocket: WebSocket, pl: str):
        await websocket.accept()
        if len(self.active_connections) < self.max_players:
            self.active_connections.append(websocket)
            self.players.append(pl)
        else:
            await websocket.send_text("mnogo")

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


game = GameRoom()
max_players = game.max_players
manager = ConnectionManager(max_players, game.players)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str, action: Action or None):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")
