from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task


def task_list(request):
    query = request.GET.get('q', '').strip()  
    tasks = Task.objects.filter(title__icontains=query) if query else Task.objects.all()

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'query': query})


def task_search(request):
    query = request.GET.get('q', '').strip()
    tasks = Task.objects.filter(title__icontains=query) if query else Task.objects.all()

    task_data = [
        {
            'id': task.id,
            'title': task.title,
            'description': task.description or "No description",
            'due_date': task.due_date.strftime('%Y-%m-%d'),
            'status': task.status
        }
        for task in tasks
    ]
    return JsonResponse({'tasks': task_data})


def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        due_date = request.POST.get('due_date')

        if not title or not due_date:  
            return render(request, 'tasks/task_form.html', {'error': "Title and Due Date are required!"})

        Task.objects.create(title=title, description=description, due_date=due_date)
        return redirect('task_list')

    return render(request, 'tasks/task_form.html')


def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.title = request.POST.get('title', '').strip()
        task.description = request.POST.get('description', '').strip()
        task.due_date = request.POST.get('due_date')

        if not task.title or not task.due_date:
            return render(request, 'tasks/task_form.html', {'task': task, 'error': "Title and Due Date are required!"})

        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
