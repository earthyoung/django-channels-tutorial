from django.contrib import admin
from app.models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
