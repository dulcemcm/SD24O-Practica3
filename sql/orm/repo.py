import orm.modelos as modelos
import orm.esquemas as esquemas
from sqlalchemy.orm import Session

# GET '/alumnos'
# select * from app.alumnos
def devuelve_alumnos(sesion:Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

#POST '/alumnos'
def guardar_alumno(sesion:Session, alumno_nuevo:esquemas.AlumnoBase):
    #1.- Crear un nuevo objeto de la clase modelo Alumno
    alumno_bd = modelos.Alumno()
    #2.- Llenamos el nuevo objeto con los parámetros que nos paso el alumno
    alumno_bd.nombre = alumno_nuevo.nombre
    alumno_bd.edad = alumno_nuevo.edad
    alumno_bd.domicilio = alumno_nuevo.domicilio
    alumno_bd.carrera = alumno_nuevo.carrera
    alumno_bd.trimestre = alumno_nuevo.trimestre
    alumno_bd.email = alumno_nuevo.email
    alumno_bd.password = alumno_nuevo.password
    #3.- Insertar el nuevo objeto a la BD
    sesion.add(alumno_bd)
    #4.- Confirmamos el cambio
    sesion.commit()
    #5.- Hacemos un refresh
    sesion.refresh(alumno_bd)
    return alumno_bd

#PUT '/alumnos/{id}'
def actualiza_alumno(sesion:Session,id_alumno:int,alumno_esquema:esquemas.AlumnoBase):
    #1.-Verificar que el alumno existe
    alumno_bd = alumno_por_id(sesion,id_alumno)
    if alumno_bd is not None:
        #2.- Actualizamos los datos del alumno en la BD
        alumno_bd.nombre = alumno_esquema.nombre
        alumno_bd.edad = alumno_esquema.edad
        alumno_bd.domicilio = alumno_esquema.domicilio
        alumno_bd.carrerra = alumno_esquema.carrera
        alumno_bd.trimestre = alumno_esquema.trimestre
        alumno_bd.email = alumno_esquema.email
        alumno_bd.password = alumno_esquema.password
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(alumno_bd)
        #5.-Imprimir los datos nuevos
        print(alumno_esquema)
        return alumno_esquema
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
    
#POST '/alumnos/{id}/calificaciones'
def guardar_calificacion(sesion:Session, cal_nueva:esquemas.CalificacionBase, id_alumno:int):
    #1.-Verificar que el alumno existe
    alumno_bd = alumno_por_id(sesion,id_alumno)
    if alumno_bd is not None:
        #1.- Crear un nuevo objeto de la clase modelo Calificacion
        cal_bd = modelos.Calificacion()
        #2.- Llenamos el nuevo objeto con los parámetros que nos paso el usuario
        cal_bd.uea= cal_nueva.uea
        cal_bd.calificacion = cal_nueva.calificacion
        #3.- Insertar el nuevo objeto a la BD
        sesion.add(cal_bd)
        #4.- Confirmamos el cambio
        sesion.commit()
        #5.- Hacemos un refresh
        sesion.refresh(cal_bd)
        return cal_bd
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta

#PUT '/calificaciones/{id}'
def actualiza_calificacion(sesion:Session,id_calificacion:int,cal_esquema:esquemas.CalificacionBase):
    cal_bd = calificacion_por_id(sesion,id_calificacion)
    if cal_bd is not None:
        cal_bd.uea = cal_esquema.uea
        cal_bd.calificacion = cal_esquema.calificacion
        sesion.commit()
        sesion.refresh(cal_bd)
        print(cal_esquema)
        return cal_esquema
    else:
        respuesta = {"mensaje":"No existe la calificación"}
        return respuesta
    
#POST '/alumnos/{id}/fotos'
def guardar_foto(sesion:Session, foto_nueva:esquemas.FotoBase, id_alumno:int):
    alumno_bd = alumno_por_id(sesion,id_alumno)
    if alumno_bd is not None:
        foto_bd = modelos.Foto()
        foto_bd.titulo = foto_nueva.titulo
        foto_bd.descripcion = foto_nueva.descripcion
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta

#PUT '/fotos/{id}'
def actualiza_foto(sesion:Session,id_foto:int,foto_esquema:esquemas.FotoBase):
    foto_bd = foto_por_id(sesion,id_foto)
    if foto_bd is not None:
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        sesion.commit()
        sesion.refresh(foto_bd)
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {"mensaje":"No existe la foto"}
        return respuesta
    
# para atender GET '/alumno/{id}'
# select * from app.alumnos where id = id_alumno
def alumno_por_id(sesion:Session,id_alumno:int):
    print("select * from app.alumnos where id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id==id_alumno).first()

# GET '/fotos'
# select * from app.fotos
def devuelve_fotos(sesion:Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Foto).all()

# GET '/fotos/{id}'
# select * from app.fotos where id = id_foto
def foto_por_id(sesion:Session,id_foto:int):
    print("select * from fotos where id = id_foto")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()

# Buscar fotos por id de alumno
# GET '/alumnos/{id}/fotos'
# select * from app.fotos where id_alumno=id
def fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.fotos where id_alumno=", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno==id_alumno).all() 

# GET '/calificaciones'
# select * from app.calificaciones
def devuelve_calificaciones(sesion:Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

# GET '/calificaciones/{id}'
# select * from app.calificaciones where id = id_calificaciones
def calificacion_por_id(sesion:Session,id_calificacion:int):
    print("select * from calificaciones where id = id_calificacion")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id==id_calificacion).first()

# GET '/alumnos/{id}/calificaciones'
# select * from app.calificaciones where id_alumno=id
def calificacion_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.calificaciones where id_alumno=", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno==id_alumno).all() 

# DELETE '/alumnos/{id}'
# delete from app.alumnos where id=id_alumno
def borra_alumno_por_id(sesion:Session,id_alumno:int):
    print("delete from app.alumnos where id=", id_alumno)
    usr = alumno_por_id(sesion, id_alumno)
    if usr is not None:
        sesion.delete(usr)
        sesion.commit()
    respuesta = {
        "mensaje": "alumno eliminado"
    }
    return respuesta

# DELETE '/alumnos/{id}/calificaciones'
# delete from app.calificaciones where id_alumno=id
def borrar_calificaciones_por_id_alumnos(sesion:Session,id_alumno:int):
    print("delete from app.calificaciones where id_alumno=",id_alumno)
    calificaciones_al = calificacion_por_id_alumno(sesion, id_alumno)
    if calificaciones_al is not None:
        for calificacion_alumno in calificaciones_al:
            sesion.delete(calificacion_alumno)
        sesion.commit()

# DELETE '/alumnos/{id}/fotos'
# delete from app.fotos where id_alumno=id
def borrar_fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("delete from app.fotos where id_alumno=",id_alumno)
    fotos_al = fotos_por_id_alumno(sesion, id_alumno)
    if fotos_al is not None:
        for foto_alumno in fotos_al:
            sesion.delete(foto_alumno)
        sesion.commit()