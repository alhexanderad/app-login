from django.contrib import admin
from users.models import CustomUser
from users.forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
  model = CustomUser
  add_form = CustomUserCreationForm
  
  fieldsets = (
    *UserAdmin.fieldsets,
      ('User role', {
          "fields": (
               'is_director',
               'is_productor',
          ),
      }),
  )
  

admin.site.register(CustomUser,CustomUserAdmin)
