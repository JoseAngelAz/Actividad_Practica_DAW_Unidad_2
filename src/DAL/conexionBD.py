from flask_mysqldb import MySQLdb
from config import DevelopmentConfig

class Conexion:

    def conexion_bd():
       cnn = MySQLdb.connect(DevelopmentConfig.MYSQL_HOST, 
                             DevelopmentConfig.MYSQL_USER, 
                             DevelopmentConfig.MYSQL_PASSWORD, 
                             DevelopmentConfig.MYSQL_DB, 
                             DevelopmentConfig.MYSQL_PORT)
       return cnn