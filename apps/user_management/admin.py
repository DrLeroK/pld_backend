from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .serializers import UserSerializer

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    model = User
    list_display = ('username', 'email', 'phone_number', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 
                'email', 
                'phone_number', 
                'first_name', 
                'last_name', 
                'password1', 
                'password2',
                'is_staff',
                'is_active'
            )}
        ),
    )
    search_fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    
    # To use the same phone number validation as in the serializer
    def save_model(self, request, obj, form, change):
        from .serializers import RegisterSerializer
        serializer = RegisterSerializer(data={
            'username': obj.username,
            'email': obj.email,
            'phone_number': obj.phone_number,
            'password': obj.password,
            'password2': obj.password
        })
        
        if not change:  # Only validate phone number on creation
            serializer.validate_phone_number(obj.phone_number)
        
        super().save_model(request, obj, form, change)
        if not change:  # Only set password on creation
            obj.set_password(obj.password)
            obj.save()

# Register the custom User model with the custom admin interface
admin.site.register(User, CustomUserAdmin)