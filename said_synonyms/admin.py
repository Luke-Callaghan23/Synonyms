from django.contrib import admin


from .models import SaidSynonym, Category

# Register your models here.
admin.site.register(SaidSynonym)
admin.site.register(Category)