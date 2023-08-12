from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'get_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description='изображение')
    def get_image(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" alt="Image" width="50" height="50" />', obj.image.url)
        else:
            return 'No Image'
        display_thumbnail.short_description = 'Image'


        # Также удалось вывести картинку при помощи функции mark_safe

        # from django.utils.safestring import mark_safe
        # if obj.image:
        #     return mark_safe(f'<img src="{obj.image.url}" width=50>')
        # else:
        #     return 'No Image'

admin.site.register(Advertisements, AdvertisementAdmin)

