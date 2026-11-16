from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from sqlalchemy.orm import Session
from app.basedatos import motor, TicketDB
from sqlalchemy import select
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],  
    allow_headers=["*"],
)

vectorizador_cat, modelo_cat = joblib.load("models/modelo_categoria.pkl")
vectorizador_pri, modelo_pri = joblib.load("models/modelo_prioridad.pkl")
print("Modelos cargados")

UMBRAL_CONFIANZA = 0.60 #ticket con confianza menor a 0.60 se revisa manualmente
MINIMO_PALABRAS = 10 #ticket con menos de 10 palabras se revisa manualmente

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
    palabras = len(ticket.texto.split())
    revision_humana = bool(confianza < UMBRAL_CONFIANZA or palabras < MINIMO_PALABRAS)
    with Session(motor) as sesion:
        fila = TicketDB(texto=ticket.texto, categoria=categoria, prioridad=prioridad,
                        confianza=confianza, revision_humana=revision_humana)
        sesion.add(fila)
        sesion.commit()
        respuesta = fila_a_diccionario(fila)

    return respuesta

@app.get("/tickets")
def listar_tickets(revision_humana: bool | None = None, prioridad: str | None = None, categoria: str | None = None):
    with Session(motor) as sesion:
        consulta = select(TicketDB)
        if revision_humana is not None:
            consulta = consulta.where(TicketDB.revision_humana == revision_humana)
        if prioridad is not None:
            consulta = consulta.where(TicketDB.prioridad == prioridad)
        if categoria is not None:
            consulta = consulta.where(TicketDB.categoria == categoria)
        consulta = consulta.order_by(TicketDB.fecha.desc())
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


