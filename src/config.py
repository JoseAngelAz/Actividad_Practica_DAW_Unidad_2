class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'ecommerce'

#diccionario con las configuraciones asociadas a la clase DevelopmentConfig
config = {
        'development':DevelopmentConfig
        }
