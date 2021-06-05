from django.contrib import admin  
from django.urls import path  
from . import views  
urlpatterns = [  
    path('home', views.home),
    path('login',views.loginPage),
    path('register_ad',views.Register_Sys),
    path('register_emp',views.Register_Emp),
    path('logout',views.logoutUser),
    path('detail/<int:id>',views.detail,name='detail'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('leave/<int:id>',views.emp_leave,name='leave'),
    path('add_leave/<int:id>',views.add_leave,name='addleave'),
    path('all_leaves',views.all_leaves,name='all_leaves'),
    path('leave_detail/<int:id>',views.leave_detail,name='leave_detail'),

]  
