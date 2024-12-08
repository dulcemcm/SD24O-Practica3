from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo.py as repo 
from sqlalchemy.orm import Session
from orm.config.py import generador_sesion


app = FastAPI()


class AlumnoBase(BaseModel):
    nombre:Optional[str]=None
    edad:int
    domicilio:str    
    carrera:str
    trimestre:str
    email:str
    
alumnos = [{
    "id": 0,
    "nombre": "Lisa Simpson",
    "edad": 18,
    "domicilio": "Av. Simpre Viva",
    "carrera":"Ingeniería biologíca",
    "trimestre": "sexto",
    "email": "lisasimpson@gmail.com"
}, {
    "id": 1,
    "nombre": "Bart Simpson",
    "edad": 20,
    "domicilio": "Av. Simpre Viva",
    "carrera": "Humanidades",
    "trimestre": "tercero",
    "email":"bartsimpson@gmail.com"
},{
    "id": 2,
    "nombre": "Milhouse Van Houten",
    "edad": 20,
    "domicilio": "Av. Simpre Viva",
    "carrera": "Ingeniería en Computación",
    "trimestre": "sexto",
    "email":"milhousen@gmail.com"
}]



@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta


@app.get("/alumnos/{id}/calificaciones/{id_calificacion}")
def calificacion_alumno_por_id(id: int, id_calificacion: int):
    print("buscando calificacion con id:", id_calificacion, " del alumno con id:", id)
    
    calificacion = {
        "id_calificacion": 0,
        "uea": "Filosofía",
        "calificacion": "B"
    }

    return calificacion

@app.get("/alumnos/{id}")
def alumnos_por_id(id:int,sesion:Session=Depends(generador_sesion)):
    print("Api consultando alumno por id")
    return repo.alumno_por_id(sesion, id)

@app.get("/alumnos/{id}/fotos")
def fotos_por_id_al(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando fotos del alumno ", id)
    return repo.fotos_por_id_alumno(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_id_al(id:int,sesion:Session=Depends(generador_sesion)):
    print("API consultando calificaciones del alumno ", id)
    return repo.calificaciones_por_id_alumno(sesion, id)

@app.get("/alumnos")
def lista_alumnos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    return repo.devuelve_alumnos(sesion)


@app.post("/alumnos")
def guardar_alumno(alumno:AlumnoBase, parametro1:str):
    print("Alumno a guardar:", alumno, ", parametro1:", parametro1)

    al_nuevo = {}
    al_nuevo["id"] = len(alumnos)
    al_nuevo["nombre"] = alumno.nombre
    al_nuevo["edad"] = alumno.edad
    al_nuevo["domicilio"] = alumno.domicilio
    al_nuevo["carrera"] = alumno.carrera
    al_nuevo["trimestre"] = alumno.trimestre

    alumnos.append(alumno)

    return al_nuevo

@app.put("/alumnos/{id}")
def actualizar_alumno(id:int, alumno:AlumnoBase):
    al_act = alumno[id]
    al_act["nombre"] = alumno.nombre
    al_act["edad"] = alumno.edad
    al_act["domicilio"] = alumno.domicilio    
    al_act["carrera"] = alumno.carrera
    al_act["trimestre"] = alumno.trimestre   

    return al_act
    
@app.delete("/alumno/{id}")
def borrar_alumno(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumnos(sesion,id)
    repo.borrar_fotos_por_id_alumno(sesion,id)
    repo.borra_alumno_por_id(sesion,id)
    return {"alumno_borrado", "ok"}


@app.get("/calificaciones/{id}")
def calificaciones_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando calificacion por id")
    return repo.calificacion_por_id(sesion, id)


@app.get("/fotos/{id}")
def foto_por_id(id:int, sesion:Session=Depends(generador_sesion)):
    print("Buscando foto por id")
    return repo.foto_por_id(sesion,id)

@app.get("/fotos")
def lista_fotos(sesion:Session=Depends(generador_sesion)):
    print("API consultando todas las fotos")
    return repo.devuelve_fotos(sesion)

@app.post("/fotos")
async def guardar_foto(titulo:str=Form(None), descripcion:str=Form(...), foto:UploadFile=File(...)):
    print("titulo:", titulo)
    print("descripcion:", descripcion)

    home_usuario=os.path.expanduser("~")
    nombre_archivo=uuid.uuid4().hex  
    extension = os.path.splitext(foto.filename)[1]
    ruta_imagen=f'{home_usuario}/fotos-ejemplo/{nombre_archivo}{extension}'
    print("guardando imagen en ruta:", ruta_imagen)

    with open(ruta_imagen,"wb") as imagen:
        contenido = await foto.read()
        imagen.write(contenido)

    return {"titulo":titulo, "descripcion":descripcion, "foto":foto.filename}