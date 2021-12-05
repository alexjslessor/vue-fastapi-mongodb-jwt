from pydantic import BaseModel
import json
import requests
from fastapi import APIRouter, FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from BybitWebsocket import BybitWebsocket
import bybit
from os import environ
# import logging
from time import sleep
from collections import deque
from sse_starlette.sse import EventSourceResponse
import asyncio
# import socketio
# from socketio.asyncio_namespace import AsyncNamespace
# from pydantic import BaseModel, ValidationError
# from typing import Any
# from logging import info



key = environ.get('API_PRIVATE_KEY')
key_secret = environ.get('PRIVATE_KEY')

ws = BybitWebsocket(wsURL="wss://stream.bybit.com/realtime", api_key=key,  api_secret=key_secret)
ws.subscribe_orderBookL2("BTCUSD")


router = APIRouter()

async def stream_gen_deck(request):
    deck = deque('0')
    while True:
        if await request.is_disconnected():
            print('disconnected')
            break
        
        d = ws.get_data("orderBookL2_25.BTCUSD")        
        if not isinstance(d, list):
            for p in d['update']:
                if len(deck) < 10:
                    deck.appendleft(p['price'])
                else:
                    deck.pop()

        await asyncio.sleep(1)
        yield {'event': 'update', 
               'data': deck[0]}

@router.get('/status/stream')
async def runStatus(request: Request):
    event_generator = stream_gen_deck(request)
    print(event_generator)
    return EventSourceResponse(event_generator)

@router.get("/coinbase_current_price")
async def coinbase_current_price():
    p = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    return p

