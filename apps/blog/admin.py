from django.contrib import admin
import models

class WelcomeAdmin(admin.ModelAdmin):
    pass

class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Welcome, WelcomeAdmin)
admin.site.register(models.About, AboutAdmin)
