from django.db import models


class Organisation(models.Model):
    name_ul = models.CharField(max_length=70, verbose_name="Имя юр. лица", help_text='Форма собственности и название')
    adress_ur = models.TextField(null=True, blank=True, verbose_name='Юр. Адрес', help_text="Полный почтовый адрес")
    adress_post = models.TextField(null=True, blank=True, verbose_name='Почтовый Адрес')
    telefon = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    e_mail = models.EmailField(max_length=20, blank=True, verbose_name='Электронная почта')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    kpp = models.CharField(max_length=9, verbose_name='КПП')
    okpo = models.CharField(max_length=12, blank=True, verbose_name='ОКПО')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Организации'
        verbose_name = 'Организация'
        ordering = ['name_ul']

    def __str__(self):
        return self.name_ul


class Material(models.Model):
    name = models.CharField(max_length=100, help_text='Введите имя материала для печати',
                            verbose_name='Материал для печати', blank=True, null=True, default=None)
    price = models.FloatField(max_length=100, help_text='Стоимость печати в руб.', verbose_name='За 1 метр квадратный')
    resolution_print = models.IntegerField(help_text='разрешение для печати на материале', verbose_name='DPI',
                                           blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    COLOR_MODE = (
        ('RGB', 'rgb'),
        ('CMYK', 'cmyk'),
        ('GREY', 'Greyscale'),
        ('LAB', 'lab')
    )

    name = models.CharField(max_length=60, verbose_name='Имя файла')
    # order = models.ForeignKey('Orders', on_delete=models.CASCADE, verbose_name='order')
    material = models.ForeignKey("Material", on_delete=models.CASCADE, verbose_name='Материал')
    # order = models.ForeignKey('Orders', on_delete=models.CASCADE, verbose_name='Заказы')
    quantity = models.IntegerField(default=1, help_text='Введите количество', verbose_name="Количество")
    width = models.FloatField(default=0, verbose_name="Ширина", help_text="Указывается в см.")
    length = models.FloatField(default=0, verbose_name="Длина", help_text="Указывается в см.")
    resolution = models.IntegerField(default=0, verbose_name="Разрешение",
                                     help_text="для баннера 72 dpi, для Пленки 150 dpi")
    color_model = models.CharField(max_length=10, choices=COLOR_MODE, verbose_name="Цветовая модель",
                                   help_text="Для корректной печати модель должна быть CMYK")
    size = models.FloatField(default=0, verbose_name="Размер в Мб")
    # price = models.FloatFeld(default=0, verbose_name="Стоимость")
    path_file = models.FileField(upload_to='image/%y_%m_%d')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update
    objects = models.Manager()
    DoesNotExist = models.Manager

    #
    def __str__(self):
        return f'{self.id}-{self.material}'

    class Meta:
        verbose_name_plural = 'единица заказа'
        verbose_name = 'Товар'

    # def save(self, *args, **kwargs):
    #     print(path_file)


class Orders(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT, verbose_name='Организация')
    dostavka = models.CharField(max_length=100, verbose_name="Способ доставки")
    status = models.CharField(max_length=100, verbose_name="Статус заказа")
    zametki = models.TextField(max_length=500, verbose_name='Для заметок')
    summa_order = models.FloatField(verbose_name='Сумма заказа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # date created
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # date update
    objects = models.Manager()
    DoesNotExist = models.Manager

    def __str__(self):
        return f'{self.id} - {self.organisation}'

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'


class UploadArhive(models.Model):
    path_file = models.FileField(upload_to='image/arhive/%y/%m/%d')
    # def un_zip(self):


