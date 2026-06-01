# Alumno 7
def validate_task_name(name):
    if not isinstance(name, str):
        return False, "El nombre de la tarea debe ser una cadena de texto."
    if len(name.strip()):
        return False, "El nombre de la tarea no puede estar vacío."
    return True



# Alumno 7
def validate_id(task_id, tasks):
    if not isinstance(task_id, str):
        return False, "El ID de la tarea debe ser una cadena de texto."
    if not task_id.isdigit():
        return False, "El ID de la tarea debe ser un número."
    for task in tasks:
        if task["id"] == task_id:
            return True
    return False, "Tarea no encontrada."


# Alumno 8
def show_error(msg):
    print(f"[ERROR] {msg}")


# Alumno 8
def show_success(msg):
    print(f"[OK] {msg}")
