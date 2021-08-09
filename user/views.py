from django.shortcuts import render,redirect
from .forms import TodoForm,TodoSearchForm,RegisterationForm,LoginForm
from django.contrib import messages
from .models import Todo
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,"home.html")

def todo_create(request):
    form=TodoForm()
    context={"form":form}
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"To Do Added Successfully !!")
            return redirect("addtodo")
        else:
            messages.error(request,"To Do Not Added,Try Again")
            context["form"]=form
            return render(request, "todo_add.html", context)

    return render(request,"todo_add.html",context)

def todo_list(request):
    todos=Todo.objects.all()
    context={}
    form=TodoSearchForm()
    context["todos"]=todos
    context["form"]=form
    if request.method=="POST":
        form=TodoSearchForm(request.POST)
        if form.is_valid():
            created_by=form.cleaned_data["created_by"]
            todos = Todo.objects.filter(created_by__contains=created_by)
            context["todos"] = todos
            return render(request, "todo_list.html", context)
        else:
            context["form"] = form
            return render(request, "todo_list.html", context)

    return render(request,"todo_list.html",context)

def todo_view(request,id):
    todo=Todo.objects.get(id=id)
    context={}
    context["todo"]=todo
    return render(request,"todo_view.html",context)

def todo_edit(request,id):
    todo=Todo.objects.get(id=id)
    form=TodoForm(instance=todo)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "To Do Added Successfully !!")
            return redirect("todolist")
        else:
            context["form"] = form
            messages.error(request, "To Do Not Added,Try Again")
            return render(request, "todo_edit.html", context)
    return render(request,"todo_edit.html",context)

def todo_remove(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect("todolist")

def user_register(request):
    form=RegisterationForm()
    context={"form":form}
    if request.method=="POST":
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context = {"form": form}
            return render(request, "registration_form.html", context)

    return render(request,"registration_form.html",context)

def user_login(request):
    form=LoginForm()
    context = {"form": form}
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                context = {"form": form}
                return render(request, "signin.html", context)
    return render(request,"signin.html",context)

def user_logout(request):
    logout(request)
    return redirect("userregister")



