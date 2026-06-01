from tasks import add_task, list_tasks, complete_task, delete_task
from storage import load_tasks, save_tasks
from utils import show_error

tasks = load_tasks()

def menu():
    print("╔═══════════════════════════╗")
    print("║----- TASKFLOW DEVOPS -----║")
    print("╚═══════════════════════════╝")
    print("")
    print("[1] Agregar tarea")
    print("[2] Listar tareas")
    print("[3] Completar tarea")
    print("[4] Eliminar tarea")
    print("")
    print("[0] Salir")
    print("____________________________")

def main():
    global tasks

    while True:
        menu()
        option = input("Selecciona una opción: ")

        if option == "1":
            name = input("Nombre de la tarea: ")
            try:
                tasks = add_task(tasks, name)
                save_tasks(tasks)
            except Exception as e:
                show_error("Error al agregar la tarea: " + str(e))

        elif option == "2":
            try:
                list_tasks(tasks)
            except Exception as e:
                show_error("Error al enlistar las tareas: " + str(e))

        elif option == "3":
            task_id = input("ID de tarea: ")
            try:
                tasks = complete_task(tasks, task_id)
            except Exception as e:
                show_error("Error al completar la tarea: " + str(e))
            save_tasks(tasks)

        elif option == "4":
            task_id = input("ID de tarea: ")
            try:
                tasks = delete_task(tasks, task_id)
            except Exception as e:
                show_error("Error al eliminar la tarea: " + str(e))
            save_tasks(tasks)

        elif option == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Selecciona una opción del 0 al 4.")

if __name__ == "__main__":
    main()
