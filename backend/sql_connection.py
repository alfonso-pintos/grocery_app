import mysql.connector
import secret_keys

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password=secret_keys.SQL_PASSWORD,
                                      host='127.0.0.1',
                                      database='grocery_store')
    return __cnx
