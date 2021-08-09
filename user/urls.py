from django.urls import path
from user import views

urlpatterns=[
    path("home",views.home,name="home"),
    path("todo/add",views.todo_create,name="addtodo"),
    path("todo/list",views.todo_list,name="todolist"),
    path("todo/<int:id>",views.todo_view,name="todoview"),
    path("todo/update/<int:id>",views.todo_edit,name="todoupdate"),
    path("todo/remove/<int:id>",views.todo_remove,name="todoremove"),
    path("accounts/register",views.user_register,name="userregister"),
    path("account/signin",views.user_login,name="signin"),
    path("account/signout",views.user_logout,name="signout")

]