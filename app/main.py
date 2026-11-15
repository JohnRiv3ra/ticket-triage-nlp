from fastapi import FastAPI, HTTPException
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

def fila_a_diccionario(fila):
    return {
        "id": fila.id,
        "fecha": fila.fecha,
        "texto": fila.texto,
        "categoria": fila.categoria,
        "prioridad": fila.prioridad,
        "confianza": fila.confianza,
        "revision_humana": fila.revision_humana
    }

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
        respuesta = fila_a_diccionario(fila)

    return respuesta

@app.get("/tickets")
def listar_tickets(revision_humana: bool | None = None, prioridad: str | None = None):
    with Session(motor) as sesion:
        consulta = select(TicketDB)
        if revision_humana is not None:
            consulta = consulta.where(TicketDB.revision_humana == revision_humana)
        if prioridad is not None:
            consulta = consulta.where(TicketDB.prioridad == prioridad)
        filas = sesion.scalars(consulta).all()
        resultado = []
        for fila in filas:
            resultado.append(fila_a_diccionario(fila))
        return resultado
    
@app.get("/tickets/{id_ticket}")
def ver_ticket(id_ticket: int):
    with Session(motor) as sesion:
        fila = sesion.get(TicketDB, id_ticket)
        if fila is None:
            raise HTTPException(status_code=404, detail="Ticket no encontrado")
        return fila_a_diccionario(fila)


