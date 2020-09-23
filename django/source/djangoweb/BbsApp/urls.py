from django.contrib import admin
from django.urls import path, include
from BbsApp   import views

urlpatterns = [
    path('index/', views.loginForm, name='loginForm'),
    path('registerForm/', views.registerForm, name='registerForm'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('bbs_list/', views.list, name='bbs_list'),
    path('bbs_registerForm/', views.bbsRegisterForm, name='bbs_registerForm'),
    path('bbs_register/', views.bbsRegister, name='bbs_register'),
    path('bbs_read/<int:id>', views.bbsRead, name='bbs_read'),  # 이렇게 get 방식에서 값을 받아온 것을 이런 형식으로 받아준다.
    path('bbs_remove/', views.bbsRemove, name='bbs_remove'),
    path('bbs_modifyForm/', views.bbsModifyForm, name='bbs_modifyForm'),
    path('bbs_modify/', views.bbsModify, name='bbs_modify'),
    path('bbs_search/', views.bbsSearch, name='bbs_search'),

]
