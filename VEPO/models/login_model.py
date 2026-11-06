from datetime import datetime
from psycopg2.extras import RealDictCursor
from controllers.connection import crear_conexion


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.conn = crear_conexion()

    def auth(self):
        if not self.conn:
            print("No se pudo establecer la conexión.")
            return None

        query_auth = """
            SELECT id_employee, username, password, id_status
            FROM agua_inmaculada.logeo
            WHERE username = %s AND password = %s;
        """

        params = (self.username, self.password)

        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query_auth, params)
                resultados = cursor.fetchall()

                if resultados:
                    return resultados[0]
                return None
        except Exception as error:
            print(f"Error en la consulta de autenticación: {error}")
            return None

    def logeo_historial(self, id_employee, username):
        """Obtiene id_status e id_rol e inserta en agua_inmaculada.log usando id_employee como id_login."""
        if not self.conn:
            print("No se pudo establecer la conexión.")
            return False

        consulta_datos = """
        SELECT l.id_status, er.id_rol 
        FROM agua_inmaculada.logeo l
        LEFT JOIN agua_inmaculada.employee_rol er ON l.id_employee = er.id_employee
        WHERE l.id_employee = %s;
            """

        query_log = """
            INSERT INTO agua_inmaculada.log (id_login, username, id_status, id_rol, date_modification)
            VALUES (%s, %s, %s, %s, NOW());
        """

        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                # 1. Obtener id_status e id_rol dinámicamente
                cursor.execute(consulta_datos, (id_employee,))
                resultado = cursor.fetchone()

                if not resultado or resultado['id_rol'] is None:
                    print(
                        f"El usuario '{username}' (ID: {id_employee}) no tiene un id_rol"
                        " válido asignado en la base de datos."
                    )

                    return False

                id_status = resultado['id_status']
                id_rol = resultado['id_rol']

                cursor.execute(
                    query_log, (id_employee, username, id_status, id_rol))
                self.conn.commit()
                print(f"Bitácora registrada con éxito: id_login={id_employee},"
                      f" id_status={id_status}, id_rol={id_rol}")
                return True

        except Exception as error:
            print(f"Error al registrar en la db: {error}")
            if self.conn:
                self.conn.rollback()
            return False
        finally:
            if self.conn:
                self.conn.close()

    @staticmethod
    def obtener_rol_por_username(self):
        """Obtiene el rol del usuario basado en su username."""

        if not self.conn:
            print("No se pudo establecer la conexión.")
            return None

        query_rol = """
            SELECT id_rol
            FROM agua_inmaculada.log 
            WHERE username = %s;
        """

        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query_rol, (self.username,))
                resultado = cursor.fetchone()

                if resultado and resultado['id_rol'] is not None:
                    return resultado['id_rol']
                else:
                    print(
                        f"El usuario '{self.username}' no tiene un id_rol válido asignado."
                    )
                    return None

        except Exception as error:
            print(f"Error al obtener el rol del usuario: {error}")
            return None
        finally:
            if self.conn:
                self.conn.close()
