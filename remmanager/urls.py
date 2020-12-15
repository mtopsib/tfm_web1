
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # отслеживание захода в админку
    path('admin/', admin.site.urls),
    # смотрим в корень приложения main
    path('', include('main.urls'))
]
