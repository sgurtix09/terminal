from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from typing import List
import json
import random
import asyncio

app = FastAPI()

# Example data storage
fake_data = {
    "BTC": {
        "candle_data": [
            {"timestamp": "2026-04-01T01:00:00Z", "open": 58000, "high": 59000, "low": 57000, "close": 58500, "volume": 100},
            {"timestamp": "2026-04-01T02:00:00Z", "open": 58500, "high": 59500, "low": 57500, "close": 59000, "volume": 150},
        ],
        "current_price": 59000
    },
    # Add more assets as needed
}

@app.get("/candle-data/{asset}")
async def get_candle_data(asset: str):
    data = fake_data.get(asset)
    if data:
        return {"candle_data": data["candle_data"]}
    return {"error": "Asset not found!"}

@app.get("/current-price/{asset}")
async def get_current_price(asset: str):
    data = fake_data.get(asset)
    if data:
        return {"current_price": data["current_price"]}
    return {"error": "Asset not found!"}

@app.websocket("/ws/{asset}")
async def websocket_endpoint(websocket: WebSocket, asset: str):
    await websocket.accept()
    while True:
        # Simulating real-time data updates
        current_price = fake_data[asset]["current_price"] + random.uniform(-10, 10)  # Random fluctuation
        await websocket.send_text(json.dumps({"asset": asset, "price": current_price}))
        
        await asyncio.sleep(1)  # Simulate delay for the next update

# Example HTML page to test WebSocket
@app.get("/")
async def get():
    return HTMLResponse("""
        <html>
            <head>
                <title>WebSocket Test</title>
            </head>
            <body>
                <h1>WebSocket Test</h1>
                <button onclick=\"connect()\">Connect</button>
                <ul id=\"messages\"></ul>
                <script>
                    var ws;
                    function connect() {
                        ws = new WebSocket("ws://localhost:8000/ws/BTC");
                        ws.onmessage = function(event) {
                            var messages = document.getElementById("messages");
                            var message = document.createElement("li");
                            message.appendChild(document.createTextNode(event.data));
                            messages.appendChild(message);
                        };
                    }
                </script>
            </body>
        </html>
    """)