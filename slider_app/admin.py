from django.contrib import admin
from django.utils.safestring import mark_safe

from slider_app.models import LogoAndContacts, Soc, SliderItem, Mail


@admin.register(LogoAndContacts)
class LogoAndContactsAdmin(admin.ModelAdmin):
    list_display = ('show_logo', 'logo_name', 'phone', 'address')
    list_display_links = ('logo_name',)
    readonly_fields = ('show_logo',)

    def show_logo(self, object):
        if object.logo:  # Если фото существует
            # Функция mark_safe указывает не экранировать символы
            return mark_safe(f"<img src='{object.logo.url}' width=50")

    show_logo.short_description = "Загруженный логотип"


@admin.register(Soc)
class SocAdmin(admin.ModelAdmin):
    list_display = ('id', 'publish', 'show_icon', 'icon', 'link', 'share', 'alt')
    list_editable = ('publish',)
    list_display_links = ('id',)
    readonly_fields = ('show_icon',)

    def show_icon(self, object):
        if object.icon:
            return mark_safe(f"<img src='{object.icon.url}' style='background-color: blue' height=30 width=30")


@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'show_image', 'publish', 'image', 'header', 'description')
    list_editable = ('publish',)
    list_display_links = ('id',)
    readonly_fields = ('show_image',)

    def show_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=150 width=auto")


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message', 'date')
    list_display_links = ('id', 'phone')
