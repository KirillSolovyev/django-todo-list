from django.shortcuts import render
from django.shortcuts import get_object_or_404
from app.models import List, Task


def todo_lists(request, pk):
    list_obj = get_object_or_404(List, id=pk)
    tasks = Task.objects.filter(list=list_obj, completed=False)
    return render(request, 'todo_list.html', context={'list': list_obj, 'tasks': tasks})


def completed_todo_lists(request, pk):
    list_obj = get_object_or_404(List, id=pk)
    tasks = Task.objects.filter(list=list_obj, completed=True)
    return render(request, 'completed_todo_list.html', context={'list': list_obj, 'tasks': tasks})
