from django.apps import AppConfig

# https://blog.doomer.su/django/change-app-title-in-the-django-admin/
# генерируется минимально-базовый класс конфигурации приложения
# Этот класс, наследуется от класса AppConfig из модуля django.apps, и может иметь аттрибуты, переопределяющиеся из класса-предка

class AppAdvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_adv'
    verbose_name = "Объявления"
