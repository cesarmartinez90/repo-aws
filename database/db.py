import pymysql

host = "database-ins-1.clq02aoosm6e.us-east-2.rds.amazonaws.com"
user = "admin"
passw = "Qazplm123."
db_name = "db_users"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=passw,
            database=db_name 
        )
        print("Successfull connection to database")
        return connection
    except Exception as err:
         print("Error", err)
    return None

def insert(id, nombre, apellido, actividad, estado, cargo, fecha):
    try:
        instruction = "INSERT INTO users VALUES("+id+",'"+nombre+"','"+apellido+"','"+actividad+"','"+estado+"','"+cargo+"','"+fecha+"');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("Usuario agregado")
    except Exception as err:
        print("Error",err)
        return None


def consulta(id):
    try:
        instruction = "SELECT * FROM users WHERE id=" + id
        connection = connection_SQL()
        cursor = connection.cursor() 
        cursor.execute(instruction)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print("Error",err)
        return None