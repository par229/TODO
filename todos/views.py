from django.shortcuts import render
from .models import TodoItem
from .forms import TodoForm

def todo_list(request):
    todos = TodoItem.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()  # 폼 초기화
    return render(request, 'todo_list.html', {'todos': todos, 'form': form})
