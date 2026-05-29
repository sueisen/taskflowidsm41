from utils import validate_task_name, validate_id, show_error, show_success

# Alumno 3
def add_task(tasks, name):
    pass


# Alumno 4
def list_tasks(tasks):
    if not tasks:
        show_error("No hay tareas registradas en el sistema.")
        return

    print("\n=== MIS TAREAS ===")
    
    for task in tasks:
        if task.get("completed", False):
            status = "Completada"  
        else: 
            status = "Pendiente" 
        
        task_id = task.get("id", "N/A")
        task_name = task.get("name", "Sin nombre")
        
        print(f"{task_id} - {task_name} ({status})")
        
    print("=" * 18)

# Alumno 5
def complete_task(tasks, task_id):
    pass


# Alumno 6
def delete_task(tasks, task_id):
    pass
