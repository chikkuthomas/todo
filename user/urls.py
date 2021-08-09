from django.urls import path
from user import views

urlpatterns=[
    path("home",views.home,name="home"),
    path("todos/add",views.todo_create,name="addtodo"),
    path("todos/list",views.todo_list,name="todolist"),
    path("todos/<int:id>",views.todo_view,name="todoview"),
    path("todos/change/<int:id>",views.todo_edit,name="todoupdate"),
    path("todos/remove/<int:id>",views.todo_remove,name="todoremove"),
    path("accounts/register",views.user_register,name="userregister"),
    path("accounts/signin",views.user_login,name="signin"),
    path("accounts/signout",views.user_logout,name="signout")

]