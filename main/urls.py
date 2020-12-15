from django.urls import path
from . import views

urlpatterns = [
    # path('about', views.about, name='about'),
    # path('operindata', views.operindata, name='operindata'),
    # path('oper_dash', views.oper_dash, name='oper_dash'),
    # path('boss_dash', views.boss_dash, name='boss_dash'),
    # path('add_task', views.add_task, name='add_task'),

    path('dash1', views.dash1, name='dash1'),
    path('end_rem', views.end_rem, name='end_rem'),
    path('add_rem', views.add_rem, name='add_rem'),
    path('', views.index, name='home')

]
