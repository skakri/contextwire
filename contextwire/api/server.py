from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from contextwire.api.routes import websockets

app = FastAPI()

app.include_router(websockets.router)

mcp = FastApiMCP(app)
mcp.mount()
