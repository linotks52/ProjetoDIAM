# views.py
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Task, Utilizador
from .forms import TaskForm, UtilizadorForm, UserForm



@login_required(login_url='/taskmanager/')
def task_list(request):
    items = Task.objects.filter(user=request.user)
    items_per_page = 5
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'taskmanager/task_list.html', context)


@login_required(login_url='/taskmanager/')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('taskmanager:task_list')
    else:
        form = TaskForm()
    return render(request, 'taskmanager/create_task.html', {'form': form})


@login_required(login_url='/taskmanager/')
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskmanager:task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskmanager/edit_task.html', {'form': form, 'task': task})


@login_required(login_url='/taskmanager/')
def change_completion(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.completed:
        task.completed="False"
    else:
        task.completed="True"
    task.save()
    return HttpResponseRedirect(reverse('taskmanager:task_list'))

@login_required(login_url='/taskmanager/')
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('taskmanager:task_list')


def signup(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        nome = request.POST['nome']

        u = User.objects.create_user(username, email, password)
        user = Utilizador(user=u, email=email, nome=nome)
        user.save()
        login(request, u)
        return HttpResponseRedirect(reverse('taskmanager:task_list'))
    else:
        return render(request, 'taskmanager/signup.html')


def logar(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('taskmanager:task_list'))
        else:
            return render(request, 'taskmanager/login.html')
    else:
        return render(request, 'taskmanager/login.html')

@login_required(login_url='/taskmanager/')
def multiple_delete(request, ids):
    for id in ids:
        task = Task.objects.get(id=id)
        task.delete()
    return HttpResponseRedirect(reverse('taskmanager:task_list'))


@login_required(login_url='/taskmanager/')
def profile(request):
    return render(request, 'taskmanager/profile.html')


@login_required(login_url='/taskmanager/')
def edit_profile(request):
    profile = request.user.utilizador
    if request.method == 'POST':
        form = UtilizadorForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('taskmanager:profile')
    else:
        form = UtilizadorForm(instance=profile)
    return render(request, 'taskmanager/edit_profile.html', {'form': form})



@login_required(login_url='/taskmanager/')
def sair(request):
    request.session.flush
    logout(request)
    return HttpResponseRedirect(reverse('taskmanager:logar'))

@login_required(login_url='/taskmanager/')
def user_list(request):
    users = Utilizador.objects.all()
    return render(request, 'taskmanager/user_list.html', {'Users': users})


@login_required(login_url='/taskmanager/')
def edit_user(request, utilizador_id):
    utilizador = Utilizador.objects.get(id=utilizador_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=utilizador)
        if form.is_valid():
            form.save()
            return redirect('taskmanager:user_list')
    else:
        form = UserForm(instance=utilizador)
    print(utilizador)
    return render(request, 'taskmanager/edit_user.html', {'form': form, 'utilizador': utilizador})

@login_required(login_url='/taskmanager/')
def delete_user(request, utilizador_id):
    utilizador = Utilizador.objects.get(id=utilizador_id)
    utilizador.delete()
    return redirect('taskmanager:user_list')

@login_required(login_url='/taskmanager/')
def multiple_delete_users(request, ids):
    for id in ids:
        utilizador = Utilizador.objects.get(id=id)
        utilizador.delete()
    return HttpResponseRedirect(reverse('taskmanager:user_list'))


def creditos(request):
    return render(request, 'taskmanager/creditos.html')

@login_required(login_url='/taskmanager/')
def users_tasks(request, utilizador_id):
    user = User.objects.get(id=utilizador_id)
    items = Task.objects.filter(user=user)
    items_per_page = 5
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'taskmanager/task_list.html', context)
