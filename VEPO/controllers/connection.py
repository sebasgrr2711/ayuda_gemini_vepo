import psycopg2
from psycopg2 import OperationalError


def crear_conexion():
    conexion = None
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="vepo",
            user="postgres",
            password="UTDsebas27",
            port="5432"
        )
        print("Conexión exitosa a PostgreSQL")
    except OperationalError as e:
        print(f"Ocurrió un error al conectar a la base de datos: {e}")

    return conexion

# Ejemplo de prueba para consultar datos


"""def probar_consulta():
    conn = crear_conexion()
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Cambia 'tu_tabla' por el nombre de una tabla real en tu BD
            cursor.execute("SELECT * FROM agua_inmaculada.employee LIMIT 5;")

            registros = cursor.fetchall()
            print("Resultado de la consulta:")
            for fila in registros:
                print(fila)

            cursor.close()
            conn.close()
            print("Conexión cerrada.")
        except Exception as error:
            print(f"Error al ejecutar la consulta: {error}")


if __name__ == "__main__":
    probar_consulta()"""
