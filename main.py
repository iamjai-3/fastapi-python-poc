from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def healthCheck():
    return "Health Check!!"
