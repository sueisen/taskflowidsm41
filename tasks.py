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
    if not validate_task_name(name):
        show_error("Nombre de tarea inválido.")
        return tasks

    new_id = str(len(tasks) + 1)
    new_task = {
        "id": new_id,
        "name": name,
        "completed": False
    }
    tasks.append(new_task)
    show_success("Tarea agregada exitosamente.")
    return tasks


# Alumno 4
def list_tasks(tasks):
    if not tasks:
        print("No hay tareas para mostrar.")
        return

    print("Lista de tareas:")
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f" {status} [{task['id']}] {task['name']}")


# Alumno 5
def complete_task(tasks, task_id):
    if not validate_id(task_id):
        show_error("ID de tarea inválido.")
        return tasks

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            show_success("Tarea completada exitosamente.")
            return tasks

    show_error("Tarea no encontrada.")
    return tasks

    for task in tasks:
        if str(task["id"]) == str(task_id):
            task["state"] = "✓"
            show_success(f"Tarea {task_id} Completada exitosamente")
            return task
    
    show_error("Tarea no encontrada")
    return tasks

# Alumno 6
def delete_task(tasks, task_id):
    if not validate_id(task_id):
        show_error("ID de tarea inválido.")
        return tasks

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            show_success("Tarea eliminada exitosamente.")
            return tasks

    show_error("Tarea no encontrada.")
    return tasks
