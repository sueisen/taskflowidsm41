from tasks import add_task, list_tasks, complete_task, delete_task
from storage import load_tasks, save_tasks

tasks = load_tasks()

def menu():
    print("\n===== TASKFLOW DEVOPS =====")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("0. Salir")

def main():
    global tasks

    while True:
        menu()
        option = input("Selecciona una opción: ")

        if option == "1":
            name = input("Nombre de la tarea: ")
            tasks = add_task(tasks, name)
            save_tasks(tasks)

        elif option == "2":
            list_tasks(tasks)

        elif option == "3":
            task_id = input("ID de tarea: ")
            tasks = complete_task(tasks, task_id)
            save_tasks(tasks)

        elif option == "4":
            task_id = input("ID de tarea: ")
            tasks = delete_task(tasks, task_id)
            save_tasks(tasks)

        elif option == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
