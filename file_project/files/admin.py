from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Orders)
admin.site.register(Organisation)