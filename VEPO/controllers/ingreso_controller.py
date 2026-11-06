from models.ingreso_model import IngresoModel
from tkinter import messagebox

def registrar_ingreso_controller(fecha, tipo_venta, cantidad_str):
    # Validaciones de negocio
    if not cantidad_str.strip():
        messagebox.showerror("Error", "El campo de cantidad no puede estar vacío.")
        return False

    try:
        cantidad = float(cantidad_str.replace(",", "."))
        if cantidad <= 0:
            messagebox.showerror("Error", "La cantidad debe ser mayor a cero.")
            return False
    except ValueError:
        messagebox.showerror("Error", "La cantidad ingresada debe ser un número válido.")
        return False

    # Llamada al Modelo para guardar en PostgreSQL
    exito = IngresoModel.guardar(fecha, tipo_venta, cantidad)
    
    if exito:
        messagebox.showinfo("Éxito", f"Ingreso de {tipo_venta} registrado correctamente.")
        return True
    else:
        messagebox.showerror("Error", "No se pudo guardar el registro en la base de datos.")
        return False