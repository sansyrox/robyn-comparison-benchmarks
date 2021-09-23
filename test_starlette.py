import uvicorn
import os

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def homepage(request):
    return PlainTextResponse("Hello, World!")

routes = [
    Route("/", endpoint=homepage)
]

app = Starlette(debug=False, routes=routes)

if __name__ == '__main__':
    uvicorn.run("test_starlette:app", port=8000, log_level="warning", workers=os.cpu_count())
