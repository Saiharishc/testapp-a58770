from fastapi import FastAPI

app = FastAPI(title="TestApp")

@app.get('/items')
async def list_items():
    return []

@app.get('/test')
async def test_endpoint():
    return {"message": "This is the test endpoint"}
