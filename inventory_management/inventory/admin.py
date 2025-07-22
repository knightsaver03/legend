
from django.contrib import admin
from django.contrib.auth.models import User
from .models import ProjectType, ExardProduct, AddUser

# class ProjectTypeAdmin(admin.ModelAdmin):
#     list_select_related = ('alpha_number', 'quantity')

# class AddUserAdmin(admin.ModelAdmin):
#     list_select_related = ('username', 'password')


admin.site.register(ProjectType)
# admin.site.register(ExardProduct)
admin.site.register(AddUser)

@admin.register(ExardProduct)
class ExardProductAdmin(admin.ModelAdmin):
    list_display = ('alpha_number', 'quantity')
    search_fields = ('alpha_number',)
