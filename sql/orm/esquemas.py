from pydantic import BaseModel

class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str

class CalificacionBase(BaseModel):
    uea:str
    calificacion:str

class FotoBase(BaseModel):
    titulo:str
    descripcion:str