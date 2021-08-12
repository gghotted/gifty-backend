from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


class GenderCategoryInline(admin.TabularInline):
    model = GenderCategory
    fields = ('is_active',)
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class PriceCategoryInline(admin.TabularInline):
    model = PriceCategory
    fields = ('is_active',)
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class AgeCategoryInline(admin.TabularInline):
    model = AgeCategory
    fields = ('is_active',)
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(AppManager)
class AppManagerAdmin(admin.ModelAdmin):
    inlines = (GenderCategoryInline, PriceCategoryInline, AgeCategoryInline)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'category', 'description', 'vendor', 'views', 'likes')
    list_display_links = list_display
    list_filter = ('gender', 'age', 'price')



admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(ProductCategory)
# admin.site.register(AppManager)
# admin.site.register(AgeCategory)
# admin.site.register(PriceCategory)
# admin.site.register(GenderCategory)
