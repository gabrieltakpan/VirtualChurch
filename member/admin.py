# user_management/admin.py
from django.contrib import admin
from .models import CustomUser, Family, FamilyMember
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'title', 'gender', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('title', 'gender', 'date_of_birth')}),
    )

class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1

class FamilyAdmin(admin.ModelAdmin):
    inlines = [FamilyMemberInline]
    list_display = ['family_name', 'address', 'city', 'state', 'country']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Family, FamilyAdmin)
