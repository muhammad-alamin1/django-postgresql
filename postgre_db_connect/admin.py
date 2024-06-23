from django.contrib import admin
from .models import ConnectDB


class ConnectDBAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'user_role', 'created_at', 'updated_at', 'comment']
    list_display_links = ['user_id', 'user_name']
    list_filter = ['user_role']
    list_per_page = 20
    search_fields = ['user_name']
    

# register site
admin.site.register(ConnectDB, ConnectDBAdmin)