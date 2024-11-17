from flask import jsonify
from DAL.conexionBD import *

#Consultar Usuarios
def listar_usuarios():
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = "SELECT * FROM Usuarios"
        cursor.execute(sql)
        datos=cursor.fetchall()
        usuarios=[]
        for fila in datos:
            usuario={'id':fila[0],'nombre':fila[1],'correo':fila[2],'contrasena':fila[3],'fecha_registro':fila[4]}
            usuarios.append(usuario)
        return jsonify({'usuarios':usuarios,'mensaje':"Usuarios Listados"})
    except Exception as e:
        return jsonify({'mensaje':"HA OCURRIDO UN ERROR" + str(type[DevelopmentConfig]) })


#listar Usuario por ID
def encontrar_usuario(usuario_id):
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = "SELECT usuario_id, nombre, correo FROM Usuarios WHERE usuario_id = '{0}'".format(usuario_id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {'id':datos[0], 'nombre':datos[1], 'correo':datos[2]}
            return jsonify({'usuario':usuario, 'mensaje':'usuario encontrado!'})
        else:
            return jsonify({'mensaje':'USUARIO NO ENCONTRADO! :C'})
    except Exception as e:
        return jsonify({'mensaje':"ERROR"})
    
#Ingresar Usuario
def insertar_usuario(request):
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = """INSERT INTO Usuarios (nombre, correo, contrasena)
        VALUES ('{0}','{1}','{2}')""".format(request.json['nombre'],
        request.json['correo'],request.json['contrasena'])
        cursor.execute(sql)
        conexion.commit() #confirma la insercion
        return jsonify({'mensaje':'usuario registrado'})
    except Exception as e:
        return jsonify({'mensaje':'ERROR'})

#Eliminar Usuario por ID
def eliminar_usuario(usuario_id):
    try:
        conexion = Conexion.conexion_bd() 
        cursor= conexion.cursor()
        sql = "DELETE FROM Usuarios WHERE usuario_id = '{0}'".format(usuario_id)
        cursor.execute(sql)
        conexion.commit()#confirma la eliminacion
        return jsonify({'mensaje':"Usuario Eliminado!"})    
    except Exception as e:
        return jsonify({'mensaje':"ERROR"})

#Actualizar Usuario
def actualizar_usuario(usuario_id, request):
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = """UPDATE Usuarios SET nombre='{0}',correo='{1}',contrasena='{2}'
        WHERE usuario_id = '{3}'""".format(request.json['nombre'],
        request.json['correo'],request.json['contrasena'],usuario_id)
        cursor.execute(sql)
        conexion.commit()#confirma la actualizacion
        return jsonify({'mensaje':"Usuario Actualizado"})
    except Exception as e:
        return jsonify({'mensaje':"Error"})
