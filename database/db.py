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

def insert():
    instruction = "INSERT INTO users VALUES(125,'Carlos','Rojas','Entrega de informe','Pendiente','Ingeniero','15/09/2024');"
    connection = connection_SQL()
    cursor = connection.cursor()
    cursor.execute(instruction)
    connection.commit()
    print("Usuario agregado")
