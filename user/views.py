from django.shortcuts import render,redirect
from .forms import TodoForm,TodoSearchForm,RegisterationForm,LoginForm
from django.contrib import messages
from .models import Todo
from django.contrib.auth import authenticate,login,logout
#decorators
from .decorators import singin_required
# Create your views here.
@singin_required
def home(request,*args,**kwargs):

    return render(request,"home.html")

@singin_required
def todo_create(request,*args,**kwargs):
    form=TodoForm()
    context={"form":form}
    if request.method=="POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            todo=form.save(commit=False)
            todo.created_by=request.user
            todo.save()

            messages.success(request,"To Do Added Successfully !!")
            return redirect("addtodo")
        else:
            messages.error(request,"To Do Not Added,Try Again")
            context["form"]=form
            return render(request, "todo_add.html", context)

    return render(request,"todo_add.html",context)

@singin_required
def todo_list(request,*args,**kwargs):
    todos=Todo.objects.filter(created_by=request.user,completed=False)
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

@singin_required
def todo_view(request,id,*args,**kwargs):
    todo=Todo.objects.get(id=id)
    context={}
    context["todo"]=todo
    return render(request,"todo_view.html",context)

@singin_required
def todo_edit(request,id,*args,**kwargs):
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

@singin_required
def todo_remove(request,id,*args,**kwargs):
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
@singin_required
def user_logout(request,*args,**kwargs):
    logout(request)
    return redirect("userregister")



