from django.urls import path
# from .views import upload_images

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add/', add, name="add"),  # форма добавления файла
    path('orders/', order_add, name="order_add"),  # форма добавления заказа
    path('login/', login, name="login"),  # форма добавления файла
    path('upload/', upload_arh, name="upload_arh"),  # загрузка архива файла
    path('material/', material, name="material"),  # вdодим материалы
    # path('profile/', profile, name="profile"),  # профиль пользователя

    path('create/', create),
    path('edit/<int:id>/', edit),
    path('delete/<int:id>/', delete),


]
