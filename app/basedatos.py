from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

motor = create_engine("sqlite:///data/tickets.db")

class Base(DeclarativeBase):
    pass

class TicketDB(Base):
    __tablename__ = "tickets"
    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str]
    categoria: Mapped[str]
    prioridad: Mapped[str]
    confianza: Mapped[float]
    revision_humana: Mapped[bool]

Base.metadata.create_all(motor)
print("Base de datos lista")
