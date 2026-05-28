from utils import validate_task_name, validate_id, show_error, show_success

# Alumno 3
def add_task(tasks, name):
    pass


# Alumno 4
def list_tasks(tasks):
    pass


# Alumno 5
def complete_task(tasks, task_id):
    if not str(task_id).isdigit():
        show_error("ID invalido o no existe")
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
    pass
