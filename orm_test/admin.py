from django.contrib import admin
from .models import OrmTestModel, Author


class ORMAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'created_at', 'updated_at', 'date', 'time', 'duration',
                    'slug', 'price', 'float_f', 'year_in_school', 'author', 'email', 'url', 'unique_code',
                    'integer_field')
    prepopulated_fields = {"slug": ("user_name",)}
    

admin.site.register(OrmTestModel, ORMAdmin)
admin.site.register(Author)
    