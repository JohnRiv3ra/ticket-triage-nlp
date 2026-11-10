from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"message": "Hola, bienvenido a la API de los tickets!"}