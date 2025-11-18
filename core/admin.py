from django.contrib import admin
from .models import Expense, Category, Tag


# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'amount', 'category', 'display_tags', 'created_at', 'updated_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'name', 'created_at',)
    filter_horizontal = ('tags',)  # <-- For nice multi-select UI

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())


    display_tags.short_description = "Tags"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('name','created_at',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('name','created_at',)

