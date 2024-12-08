import orm.modelos as modelos
from sqlalchemy.orm import Session

# GET '/alumnos'
# select * from app.alumnos
def devuelve_alumnos(sesion:Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumno).all()

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