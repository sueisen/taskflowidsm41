import json
from utils import show_error
# Alumno 9
def save_tasks(tasks):
    try:
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        show_error("Error al guardar las tareas: " + str(e))


# Alumno 10
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except Exception as e:
        show_error("Error al cargar las tareas: " + str(e))
        return []
