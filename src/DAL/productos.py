from flask import jsonify
from DAL.conexionBD import *

#Consultar Productos
def listar_productos():
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = "SELECT producto_id, pr.nombre, pr.descripcion, precio, stock, cat.nombre categoria  "
        sql += "FROM productos pr inner join categorias cat on pr.categoria_id = cat.categoria_id  "
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos = []
        for fila in datos:
            producto = {'producto_id' : fila[0], 
                       'nombre' : fila[1],
                       'descripcion' : fila[2],
                       'precio' : fila[3],
                       'stock' : fila[4],
                       'categoria' : fila[5]
                       }
            productos.append(producto)
        return jsonify({'productos' : productos,'mensaje' : "Productos"})
    except Exception as e:
        return jsonify({'mensaje': 'ERROR ' + str(e)})

#listar Producto por ID
def encontrar_producto(producto_id):
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = "SELECT producto_id, pr.nombre, pr.descripcion, precio, stock, cat.nombre categoria  "
        sql += "FROM productos pr inner join categorias cat on pr.categoria_id = cat.categoria_id  WHERE producto_id = '{0}'".format(producto_id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            producto = {'producto_id' : datos[0], 
                       'nombre' : datos[1],
                       'descripcion' : datos[2],
                       'precio' : datos[3],
                       'stock' : datos[4],
                       'categoria' : datos[5]
                       }
            return jsonify({'producto' : producto, 'mensaje':'producto encontrado!'})
        else:
            return jsonify({'mensaje':'PRODUCTO NO ENCONTRADO!'})
    except Exception as e:
        return jsonify({'mensaje': 'ERROR ' + str(e)})
    
#Ingresar Producto
def insertar_producto(request):
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = """INSERT INTO productos (nombre, descripcion, precio, stock, categoria_id)
        VALUES ('{0}','{1}',{2},{3},{4})""".format(
        request.json['nombre'],
        request.json['descripcion'],
        request.json['precio'],
        request.json['stock'],
        request.json['categoria']
        )
        cursor.execute(sql)
        conexion.commit() 
        return jsonify({'mensaje' : 'Producto registrado'})
    except Exception as e:
        return jsonify({'mensaje': 'ERROR ' + str(e)})

#Eliminar Producto por ID
def eliminar_producto(producto_id):
    try:
        conexion = Conexion.conexion_bd() 
        cursor= conexion.cursor()
        sql = "DELETE FROM Productos WHERE producto_id = '{0}'".format(producto_id)
        cursor.execute(sql)
        conexion.commit() 
        return jsonify({'mensaje' : "Producto Eliminado!"})    
    except Exception as e:
        return jsonify({'mensaje' : 'ERROR ' + str(e)})

#Actualizar Producto
def actualizar_producto(producto_id, request):
    try:
        conexion = Conexion.conexion_bd()
        cursor = conexion.cursor()
        sql = """UPDATE Productos SET nombre='{0}', descripcion='{1}', precio={2}, stock={3}, categoria_id={4}
        WHERE producto_id = '{5}'""".format(
        request.json['nombre'],
        request.json['descripcion'],
        request.json['precio'], 
        request.json['stock'],
        request.json['categoria'],
        producto_id)
        cursor.execute(sql)
        conexion.commit()
        return jsonify({'mensaje' : 'Producto Actualizado'})
    except Exception as e:
        return jsonify({'mensaje' : 'ERROR ' + str(e)})