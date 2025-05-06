from pydantic import BaseModel

class Product(BaseModel):
    nombre: str
    tipo: str
    descripcion: str
    meses: list[str]
    regiones: list[str]
    imagen: str