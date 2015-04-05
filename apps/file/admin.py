from django.contrib import admin
import models

class FileAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.File, FileAdmin)
