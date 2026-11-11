from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from sqlalchemy.orm import Session
from app.basedatos import motor, TicketDB
from sqlalchemy import select



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
    with Session(motor) as sesion:
        fila = TicketDB(texto=ticket.texto, categoria=categoria, prioridad=prioridad,
                        confianza=confianza, revision_humana=revision_humana)
        sesion.add(fila)
        sesion.commit()
        id_ticket = fila.id

    return {"id": id_ticket, "categoria": categoria, "prioridad": prioridad, "confianza": confianza, "revision_humana": revision_humana}

@app.get("/tickets")
def listar_tickets():
    with Session(motor) as sesion:
        filas = sesion.scalars(select(TicketDB)).all()
        resultado = []
        for fila in filas:
            resultado.append({"id": fila.id, "texto": fila.texto, "categoria": fila.categoria, "prioridad": fila.prioridad, "confianza": fila.confianza, "revision_humana": fila.revision_humana})
    return resultado

