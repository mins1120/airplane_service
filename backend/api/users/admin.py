from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')  # 'username' 대신 'email' 사용
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, UserAdmin)
