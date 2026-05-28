def validate_task_name(name):
    return name is not None and name.strip() != ""


def validate_id(task_id, tasks):
    return any(str(t["id"]) == str(task_id) for t in tasks)


def show_error(msg):
    print(f"[ERROR] {msg}")


def show_success(msg):
    print(f"[OK] {msg}")