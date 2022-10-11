from quart import Quart, request

app = Quart(__name__)


@app.route("/api/search")
async def search():
    req = requests.get(
        f"https://dummyjson.com/products/search?q={request.args.get('query', type=str)}"
    )
    return {"response": req.json()}
