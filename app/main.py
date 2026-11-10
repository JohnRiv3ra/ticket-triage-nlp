from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

vectorizador_cat, modelo_cat = joblib.load("models/modelo_categoria.pkl")
vectorizador_pri, modelo_pri = joblib.load("models/modelo_prioridad.pkl")
print("Modelos cargados")

class Ticket(BaseModel):
    texto: str

@app.get("/")
def inicio():
    return {"message": "Hola, bienvenido a la API de los tickets!"}

@app.post("/clasificar")
def clasificar(ticket: Ticket):
    nuevo = [ticket.texto]
    x_cat = vectorizador_cat.transform(nuevo)
    x_pri = vectorizador_pri.transform(nuevo)
    categoria = modelo_cat.predict(x_cat)[0]
    prioridad = modelo_pri.predict(x_pri)[0]
    confianza = round(modelo_cat.predict_proba(x_cat).max(), 2)
    revision_humana = bool(confianza < 0.60)
    return {"categoria": categoria, "prioridad": prioridad, "confianza": confianza, "revision_humana": revision_humana}


