from flask import Flask, request
from DAL import usuarios, productos

app = Flask(__name__)

#INICIO ENTIDAD USUARIOS
#Consultar Usuarios
@app.route('/Usuarios', methods=['GET'])
def listar_usuarios():
        return usuarios.listar_usuarios()

#listar Usuario por ID
@app.route('/Usuarios/<usuario_id>', methods=['GET'])
def encontrar_usuario(usuario_id):
         return usuarios.encontrar_usuario(usuario_id)
 
#Ingresar Usuario
@app.route('/Usuarios', methods=['POST'])
def insertar_usuario():
         return usuarios.insertar_usuario(request)
  
#Eliminar Usuario por ID
@app.route('/Usuarios/<usuario_id>', methods=['DELETE'])
def eliminar_usuario(usuario_id):
        return usuarios.eliminar_usuario(usuario_id)   

#Actualizar Usuario
@app.route('/Usuarios/<usuario_id>', methods=['PUT'])
def actualizar_usuario(usuario_id):
        return usuarios.actualizar_usuario(usuario_id, request)   

#INICIO ENTIDAD PRODUCTOS
#Consultar Productos
@app.route('/Productos', methods=['GET'])
def listar_productos():
        return productos.listar_productos()

#Consultar Producto por ID
@app.route('/Productos/<producto_id>', methods=['GET'])
def encontrar_producto(producto_id):
         return productos.encontrar_producto(producto_id)

#Ingresar Producto
@app.route('/Productos', methods=['POST'])
def insertar_producto():
         return productos.insertar_producto(request)

#Eliminar Producto por ID
@app.route('/Productos/<producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
        return productos.eliminar_producto(producto_id)   

#Actualizar Producto
@app.route('/Productos/<producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
        return productos.actualizar_producto(producto_id, request)  

def pagina_no_encontrada(error):
    return "<h1> LA PAGINA QUE INTENTAS BUSCAR NO EXISTE!</h1>", 404

if __name__ == '__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()

