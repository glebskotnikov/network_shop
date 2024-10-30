from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Product, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role_type", "supplier_link", "city", "debt")
    list_filter = ("city",)
    actions = ["clear_debt"]

    def role_type(self, obj):
        return obj.role if obj.role else "No role"

    role_type.short_description = "Role Type"

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:users_user_change", args=[obj.supplier.id])
            link = format_html('<a href="{}">{}</a>', url, obj.supplier)
            return link
        return "No supplier"

    supplier_link.short_description = "Supplier"

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Clear debt for selected users"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "model", "release_date")
