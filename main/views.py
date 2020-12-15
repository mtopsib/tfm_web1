from django.shortcuts import render, redirect

# from .forms import InDataForm
from .models import GrpStatDown, TechType, WorkArea, TechRole, Vinechikle, StateDown, DownTimeJornal, UpTimeJornal


def index(request):
    spi = DownTimeJornal.objects.all()

    # TODO формируем список оборудования вставшего на ремонт

    # TODO формируем список орборудования вышедшего с ремонта

    # TODO формируем списки тех кто еще в ремонте

    # TODO формируем список тех кто уже починился

    return render(request, 'main\\index.html', {'title': 'index Главная страница сайта', 'spi': spi})


def dash1(request):
    return render(request, 'main\\dash1.html', {'title': 'Dashboard 1'})


def add_rem(request):
    return render(request, 'main\\add_rem.html', {'title': 'add_rem Главная страница сайта'})


def end_rem(request):
    return render(request, 'main\\end_rem.html', {'title': 'end_rem Главная страница сайта'})



