from utils import validate_task_name, validate_id, show_error, show_success


# Alumno 2 - Brando
# Modelo de datos para almacenar las tareas

ESTADO_PENDIENTE = "pendiente"
ESTADO_COMPLETADA = "completada"


def crear_modelo_tarea(task_id, nombre):
    return {
        "id": task_id,
        "nombre": nombre,
        "estado": ESTADO_PENDIENTE
    }


# Alumno 3
def add_task(tasks, name):
    pass


# Alumno 4
def list_tasks(tasks):
    pass


# Alumno 5
def complete_task(tasks, task_id):
    pass


# Alumno 6
def delete_task(tasks, task_id):
    pass
