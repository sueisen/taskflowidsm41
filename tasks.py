from utils import validate_task_name, validate_id, show_error, show_success

#

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
    # validacion
    resultado_validacion = validate_task_name(name)
    
    # si validacion falla mostrar un error
    if isinstance(resultado_validacion, tuple):
        valido = resultado_validacion[0]
        mensaje_error = resultado_validacion[1]
        if not valido:
            show_error(mensaje_error)
            return tasks
            
    # si validacion falla mostrar un error
    elif resultado_validacion == False:
        show_error("Nombre de tarea inválido.")
        return tasks

    #asignacion de id empezando la lista por 1
    id_mas_alto = 0
    
    # obtencion de id mas alto para asignar el siguient id 
    for tarea in tasks:
        id_actual_str = tarea["id"]
        # verificacion de id valida para convertir a entero
        if id_actual_str.isdigit():
            id_actual_int = int(id_actual_str)
            if id_actual_int > id_mas_alto:
                id_mas_alto = id_actual_int
                
    # se asigna el nuevo id mas alto
    nuevo_id_int = id_mas_alto + 1
    new_id = str(nuevo_id_int)


    nombre_limpio = name.strip()
    
    new_task = {
        "id": new_id,
        "name": nombre_limpio,
        "completed": False
    }

    # Guardamos cuántas tareas había antes de agregar la nueva
    longitud_inicial = len(tasks)
    
    #se agrega a la lista la nueva tarea
    tasks.append(new_task)


    longitud_final = len(tasks)
    ultima_tarea = tasks[-1]
    
    # verifica si la lista realmente ha crecido en 1 si la respuesta es que si manda un mensaje de cnfirmacion
    if longitud_final == longitud_inicial + 1 and ultima_tarea["id"] == new_id:
        show_success(f"Tarea '{nombre_limpio}' guardada y registrada correctamente con el ID: {new_id}.")
    else:
        #en caso de que no se agregue correctamente se muestra un error
        show_error("Error de consistencia: La nueva entrada no se pudo guardar en la lista.")

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
