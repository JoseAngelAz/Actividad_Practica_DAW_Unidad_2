from MySQLdb.cursors import Cursor
from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
conexion=MySQL(app)

#Consultar Usuarios
@app.route('/Usuarios', methods=['GET'])
def listar_usuarios():
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT * FROM Usuarios"
        cursor.execute(sql)
        datos=cursor.fetchall()
        usuarios=[]
        for fila in datos:
            usuario={'id':fila[0],'nombre':fila[1],'correo':fila[2],'contrasena':fila[3],'fecha_registro':fila[4]}
            usuarios.append(usuario)
        return jsonify({'usuarios':usuarios,'mensaje':"Usuarios Listados"})
    except Exception as e:
        return jsonify({'mensaje':"HA OCURRIDO UN ERROR"})

#listar Usuario por ID
@app.route('/Usuarios/<usuario_id>', methods=['GET'])
def encontrar_usuario(usuario_id):
    try:
        cursor = conexion.connection.cursor()
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
@app.route('/Usuarios', methods=['POST'])
def insertar_usuario():
    try:
        cursor=conexion.connection.cursor()
        sql = """INSERT INTO Usuarios (nombre, correo, contrasena)
        VALUES ('{0}','{1}','{2}')""".format(request.json['nombre'],
        request.json['correo'],request.json['contrasena'])
        cursor.execute(sql)
        conexion.connection.commit()#confirma la insercion
        return jsonify({'mensaje':'usuario registrado'})
    except Exception as e:
        return jsonify({'mensaje':'ERROR'})


#Eliminar Usuario por ID
@app.route('/Usuarios/<usuario_id>', methods=['DELETE'])
def elimnar_usuario(usuario_id):
    try: 
        cursor= conexion.connection.cursor()
        sql = "DELETE FROM Usuarios WHERE usuario_id = '{0}'".format(usuario_id)
        cursor.execute(sql)
        conexion.connection.commit()#confirma la eliminacion
        return jsonify({'mensaje':"Usuario Eliminado!"})    
    except Exception as e:
        return jsonify({'mensaje':"ERROR"})

#Actualizar Usuario
@app.route('/Usuarios/<usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
    try:
        cursor = conexion.connection.cursor()
        sql = """UPDATE Usuarios SET nombre='{0}',correo='{1}',contrasena='{2}'
        WHERE usuario_id = '{3}'""".format(request.json['nombre'],
        request.json['correo'],request.json['contrasena'],usuario_id)
        cursor.execute(sql)
        conexion.connection.commit()#confirma la actualizacion
        return jsonify({'mensaje':"Usuario Actualizado"})
    except Exception as e:
        return jsonify({'mensaje':"Error"})

def pagina_no_encontrada(error):
    return "<h1> LA PAGINA QUE INTENTAS BUSCAR NO EXISTE!</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()

