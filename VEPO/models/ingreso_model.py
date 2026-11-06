from datetime import datetime
from controllers.connection import crear_conexion


class IngresoModel:

    @staticmethod
    def obtener_id_employee_por_username(username):
        conexion = crear_conexion()
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                query = """
                    SELECT id_employee 
                    FROM agua_inmaculada.logeo 
                    WHERE username = %s;
                """
                cursor.execute(query, (username,))
                resultado = cursor.fetchone()
                cursor.close()
                conexion.close()
                if resultado:
                    return resultado[0]
                return None
            except Exception as error:
                print(f"Error en base de datos al obtener empleado: {error}")
                if conexion:
                    conexion.close()
                return None
        return None

    @staticmethod
    def obtener_ventas():
        conexion = crear_conexion()
        ventas = []
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                query = """
                    SELECT date, type, amount 
                    FROM agua_inmaculada.sells
                    ORDER BY id_sell DESC;
                """
                cursor.execute(query)
                registros = cursor.fetchall()
                cursor.close()
                conexion.close()
                for reg in registros:
                    fecha_fmt = (reg[0].strftime(
                        "%d/%m/%Y") if isinstance(reg[0], datetime) else str(reg[0]))
                    ventas.append(
                        (fecha_fmt, {"tipo": reg[1], "cantidad": reg[2]}))
            except Exception as error:
                print(f"Error en base de datos al obtener ventas: {error}")
                return ventas

                if conexion:
                    conexion.close()
                return []
            return []

    @staticmethod
    def guardar(id_employee, fecha_str, tipo_venta, cantidad):
        """Guarda un registro de venta en la tabla agua_inmaculada.sells."""
        conexion = crear_conexion()
        if conexion is not None:
            try:
                # Convertir fecha de DD/MM/YYYY a YYYY-MM-DD para PostgreSQL
                fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y")
                fecha_sql = fecha_obj.strftime("%Y-%m-%d")

                cursor = conexion.cursor()
                query = """
                    INSERT INTO agua_inmaculada.sells (id_employee, date, type, amount) 
                    VALUES (%s, %s, %s, %s);
                """
                cursor.execute(
                    query, (id_employee, fecha_sql, tipo_venta, cantidad))
                conexion.commit()
                cursor.close()
                conexion.close()
                if cursor.rowcount > 0:
                    print("Ingreso guardado correctamente.")
                return True
            except ValueError:
                print("Error: Formato de fecha inválido. Usar dd/mm/aaaa")
                if conexion:
                    conexion.close()
                return False
            except Exception as error:
                print(f"Error en base de datos al guardar ingreso: {error}")
                if conexion:
                    conexion.close()
                return False
        return False
