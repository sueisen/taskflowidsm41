from utils import validate_task_name, validate_id, show_error, show_success

def add_task(tasks, name):
    if not validate_task_name(name):
        show_error("Nombre inválido")
        return tasks

    new_task = {
        "id": len(tasks) + 1,
        "name": name,
        "done": False
    }

    tasks.append(new_task)
    show_success("Tarea agregada")
    return tasks


def list_tasks(tasks):
    print("\n--- LISTA DE TAREAS ---")
    for t in tasks:
        status = "✔" if t["done"] else "❌"
        print(f'{t["id"]} - {t["name"]} [{status}]')


def complete_task(tasks, task_id):
    for t in tasks:
        if str(t["id"]) == str(task_id):
            t["done"] = True
            show_success("Tarea completada")
            return tasks

    show_error("Tarea no encontrada")
    return tasks


def delete_task(tasks, task_id):
    for t in tasks:
        if str(t["id"]) == str(task_id):
            tasks.remove(t)
            show_success("Tarea eliminada")
            return tasks

    show_error("Tarea no encontrada")
    return tasks