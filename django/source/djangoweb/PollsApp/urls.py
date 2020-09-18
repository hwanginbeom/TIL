from django.contrib import admin
from django.urls import path, include
from PollsApp   import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:question_id>/', views.choice, name='choice'),  # 여기서는 int형이라고 알리는 것 뿐 이다.
    path('vote/', views.vote, name='vote'),
    path('result/', views.result, name='result')
]
