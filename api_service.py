from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    """Simple health check endpoint returning a pong message."""
    return {"message": "pong"}
