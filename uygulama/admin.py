from django.contrib import admin
from uygulama.models import uygulama

class UygulamaAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    class Meta:
        model = uygulama

admin.site.register(uygulama,UygulamaAdmin)