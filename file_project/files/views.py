import os
# import zipfile
import patoolib

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .models import Product, Material
from .forms import UploadFiles, OrdersAdd, UploadArhive

menu = [{'title': 'О сайте', "url_name": 'about'},
        {'title': "Добавить файлы", "url_name": 'add'},
        {'title': "Обратная связь", "url_name": 'contact'},
        {'title': "Войти", "url_name": 'login'}
        ]


def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")


def login(request):
    pass


def index(request):
    product = Product.objects.all()
    return render(request, "files/index.html", {"product": product, 'title': 'Загрузка файлов', 'menu': menu})


def material(request):
    product = Material.objects.all()
    return render(request, "files/material.html", {"product": product, 'title': 'Материалы', 'menu': menu})

# def profile(request):
#     product = Profile.objects.all()
#     return render(request, "files/profile.html", {"product": product, 'title': 'Профиль', 'menu': menu})


def create(request):
    if request.method == "POST":
        product = Product()
        # product.name = request.POST.get('name')
        # product.material = request.POST.get("material")

        product.quantity = request.POST.get('quantity')
        # product.order =
        product.width = request.POST.get('width')
        product.length = request.POST.get('length')
        # product.resolution = 300
        # product.color_model = request.POST.get('color_model')
        # product.size = 1000
        # product.price = 5000
        product.path_file = request.POST.get('path_file')
        # product.created_at
        # product.updated_at
        product.save()

        return HttpResponseRedirect("/")


def add(request):
    if request.POST:
        form = UploadFiles(request.POST, request.FILES)
        print(request.FILES['path_file'])
        if form.is_valid():
            # file_name_add(request.FILES['path_file'])

            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UploadFiles

    return render(request, 'files/add.html',
                  {'form': form, 'menu': menu, 'title': 'Добавление файлов'})  # изменение данных в БД


def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.POST:
            # product.name = request.POST.get("name")
            product.material = request.POST.get("material")
            product.quantity = request.POST.get("quantity")
            product.width = request.POST.get("width")
            product.length = request.POST.get("length")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "files/edit.html",
                          {"product": product, 'menu': menu, 'title': 'Редактрирование файлов'})

    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")


def order_add(request):
    if request.POST:
        form = OrdersAdd(request.POST)
        if form.is_valid():
            # file_name_add(request.FILES['path_file'])

            form.save()
            return HttpResponseRedirect("/")
    else:
        form = OrdersAdd

    return render(request, 'files/orders_add.html',
                  {'form': form, 'menu': menu, 'title': 'Новый заказ'})  # изменение данных в БД


def unzip(arh_name):
    # with zipfile.ZipFile(arh_name) as zf:
    #     zf.extractall('image/arh')
    patoolib.extract_archive(str(arh_name), outdir="image/arh/test")


def upload_arh(request):
    if request.POST:
        form = UploadArhive(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data['path_file'])
            arh_name = form.cleaned_data['path_file']
            print(type(arh_name))
            form.save()
            unzip(arh_name)

            return HttpResponseRedirect("/")
    else:
        form = UploadArhive

    return render(request, 'files/up_arh.html',
                  {'form': form, 'menu': menu, 'title': 'Добавление файлов'})  # изменение данных в БД
