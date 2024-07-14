from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'pub_date']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']

class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file', 'file-type', 'is_enable']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'pub_date']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories']
    inlines = [FileInlineAdmin]
