from django.contrib import admin
from django.utils.html import mark_safe
from comic.models import *

class MyComicAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'created_date', 'updated_date', 'status', 'view_count', 'description']
    search_fields = ['name']
    list_filter = ['id', 'created_date', 'name']
    readonly_fields = ['my_image']

    def my_image(self, instance):
        if instance:
            return mark_safe(f"<img width='120' src='/static/{instance.image.name}'/>")


admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(Writer)
admin.site.register(Comic, MyComicAdmin)
admin.site.register(Chapter)
admin.site.register(Page)
admin.site.register(History)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Reaction)
