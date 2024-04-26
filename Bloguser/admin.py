# from django.contrib import admin
# from .models import CustomUser
# # Register your models here.
# class UserServiceAdmin(admin.ModelAdmin):
#     list_display=['id','username','email','date_joined']
#     list_display_links=['id','username','email']
#     list_filter=[]


# admin.site.register(CustomUser,UserServiceAdmin)

from django.contrib import admin
from .models import CustomUser

# Define the ModelAdmin class for CustomUser
class UserServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'date_joined']
    list_display_links = ['id', 'username', 'email']
    list_filter = []

# Register the CustomUser model with the UserServiceAdmin class
admin.site.register(CustomUser, UserServiceAdmin)