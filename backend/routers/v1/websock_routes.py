from fastapi import (APIRouter, 
                     Request, 
                     Depends)
from json import dumps, loads
from fastapi import WebSocket


router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    
    await websocket.accept()
    
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"{data}")