from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello! Meri pehli Python web app successfully chal rahi hai 🚀"}