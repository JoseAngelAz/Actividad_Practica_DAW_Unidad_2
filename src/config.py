class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PORT = 3307 # por defecto es el 3306
    MYSQL_PASSWORD = '' # colocar la contrasena que le hayan colocado al mysql
    MYSQL_DB = 'ecommerce'

#diccionario con las configuraciones asociadas a la clase DevelopmentConfig
config = {
        'development':DevelopmentConfig
        }
