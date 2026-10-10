import json
from pathlib import Path
from datetime import date, timedelta
from nicegui import ui


TASKS_FILE = Path(__file__).with_name('tasks.json')

def load_tasks():
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open('r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        ui.notify(
            'Could not read tasks.json. Starting with an empty list.',
            type='warning'
        )
        return []


def save_tasks():
    with TASKS_FILE.open('w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

tasks = load_tasks()

next_task_id = max(
    (task.get('id', 0) for task in tasks),
    default=0
) + 1

next_task_id = 1

ui.label('My To-Do App').classes('text-3xl font-bold')
ui.label('Manage your tasks and deadlines').classes('text-gray-500')

# Dashboard statistics
with ui.grid(columns=2).classes('w-full max-w-xl gap-4'):
    total_label = ui.label().classes('text-xl font-bold')
    completed_label = ui.label().classes('text-xl font-bold')
    pending_label = ui.label().classes('text-xl font-bold')
    progress_label = ui.label().classes('text-xl font-bold')

progress_bar = ui.linear_progress(value=0).classes('w-full max-w-xl')

task_input = ui.input(
    label='Task name',
    placeholder='Enter a task...'
).classes('w-full max-w-md')

deadline_input = ui.date(
    value=date.today().isoformat()
).classes('w-full max-w-md')

task_list = ui.column().classes('w-full max-w-xl')


def add_task():
    global next_task_id
    name = (task_input.value or '').strip()
    deadline = deadline_input.value
    if not name:
        ui.notify('Please enter a task name', type='warning')
        return
    tasks.append({
        'id': next_task_id,
        'name': name,
        'deadline': deadline,
        'done': False,
    })
    next_task_id += 1
    save_tasks()
    task_input.value = ''
    show_tasks()
    ui.notify('Task added!')

def edit_task(task):
    with ui.dialog() as dialog, ui.card().classes('w-full max-w-md'):
        ui.label('Edit Task').classes('text-xl font-bold')
        name_input = ui.input(
            label='Task name',
            value=task['name']
        ).classes('w-full')

        date_input = ui.date(
            value=task['deadline'] or date.today().isoformat()
        ).classes('w-full')

        def save_changes():
            new_name = (name_input.value or '').strip()

            if not new_name:
                ui.notify('Task name cannot be empty', type='warning')
                return

            task['name'] = new_name
            task['deadline'] = date_input.value
            save_tasks()
            show_tasks()
            dialog.close()
            ui.notify('Task updated!')

        with ui.row():
            ui.button('Save Changes', on_click=save_changes)
            ui.button('Cancel', on_click=dialog.close).props('flat')

    dialog.open()


def mark_done(task, value):
    task['done'] = value
    save_tasks()
    show_tasks()

def delete_task(task):
    tasks.remove(task)
    save_tasks()
    show_tasks()
    ui.notify('Task deleted')

def update_dashboard():
    total = len(tasks)

    completed = sum(
        1 for task in tasks if task['done']
    )

    pending = total - completed

    progress = completed / total if total > 0 else 0

    total_label.set_text(f'Total Tasks: {total}')
    completed_label.set_text(f'Completed: {completed}')
    pending_label.set_text(f'Pending: {pending}')
    progress_label.set_text(
        f'Progress: {progress * 100:.1f}%'
    )

    progress_bar.set_value(progress)

def get_deadline_status(task):
    if task['done']:
        return 'Completed', 'positive'

    deadline = task.get('deadline')

    if not deadline:
        return 'No deadline', 'grey'

    due_date = date.fromisoformat(deadline)
    today = date.today()

    if due_date < today:
        return 'Overdue', 'negative'
    elif due_date == today:
        return 'Due today', 'warning'
    elif due_date <= today + timedelta(days=3):
        return 'Due soon', 'warning'
    else:
        return 'Upcoming', 'positive'

def show_tasks():
    update_dashboard()
    task_list.clear()

    with task_list:
        if not tasks:
            ui.label('No tasks yet. Add your first task!')
            return

        for task in tasks:
            with ui.card().classes('w-full'):
                with ui.row().classes('items-center w-full'):
                    ui.checkbox(
                        value=task['done'],
                        on_change=lambda e, t=task: mark_done(t, e.value)
                    )
                    with ui.column().classes('gap-1'):
                        ui.label(task['name']).classes('font-bold text-lg')

                        ui.label(
                            f"Deadline: {task['deadline'] or 'Not set'}"
                        ).classes('text-gray-500')

                        status, color = get_deadline_status(task)
                        ui.badge(status, color=color)

                    if task['done']:
                        ui.badge('Completed', color='positive')

                with ui.row():
                    ui.button(
                        'Edit',
                        icon='edit',
                        on_click=lambda t=task: edit_task(t)
                    ).props('outline')

                    ui.button(
                        'Delete',
                        icon='delete',
                        on_click=lambda t=task: delete_task(t)
                    ).props('outline color=negative')


ui.button('Add Task', on_click=add_task)
ui.separator()
show_tasks()

ui.run(title='My To-Do App')