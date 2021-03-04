from django.shortcuts import render


def get_todos():
    todos = []
    for i in range(10):
        todos.append({
            'name': 'Task' + str(i + 1),
            'created': '11/12/2021',
            'due_on': '20/12/2021',
            'owner': 'admin',
            'status': 'done' if i < 2 else 'active'
        })
    return todos


def todo_lists(request):
    todos = get_todos()
    uncompleted = [todo for todo in todos if not todo['status'] == 'done']
    return render(request, 'todo_list.html', context={'todos': uncompleted})


def completed_todo_lists(request):
    todos = get_todos()
    uncompleted = [todo for todo in todos if not todo['status'] != 'done']
    return render(request, 'completed_todo_list.html', context={'todos': uncompleted})
