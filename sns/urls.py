from django.urls import path
from . import views

urlpatterns = [
    path('', views.redir_top),
    path('top/', views.top, name='top'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.mylogin, name='login'),
    path('alltweet/', views.alltweet, name='alltweet'),
    path('logout/', views.log_out, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('othre/<str:name>', views.other, name='other')
]