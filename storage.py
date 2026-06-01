from utils import show_error
# Alumno 9
def save_tasks(tasks):
    try:
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"{task['id']},{task['name']},{task['completed']}\n")
    except Exception as e:
        show_error("Error al guardar las tareas: " + str(e))

 


# Alumno 10
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = []
            for line in file:
                id, name, completed = line.strip().split(",")
                tasks.append({
                    "id": id,
                    "name": name,
                    "completed": completed == "True"
                })
        return tasks
    except Exception as e:
        show_error("Error al cargar las tareas: " + str(e))
        return []
