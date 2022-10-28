from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog.models import LiteraryFormat, Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "format"]
    list_filter = ["format"]
    search_fields = ["title"]


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("pseudonym",)
    fieldsets = UserAdmin.fieldsets + ((
        "Additional info", {"fields": ("pseudonym",)},
    ),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        "Additional info", ("first_name", "last_name", {"fields": "pseudonym"},)
    )


admin.site.register(LiteraryFormat)
