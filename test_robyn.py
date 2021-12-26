from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
async def h(_):
    return "Hello, world!"

app.start(port=5002)
