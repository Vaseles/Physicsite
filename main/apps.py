from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

# class MainConfig(AppConfig):
#     name = 'full.python.path.to.your.app.main'
#     label = 'main'  # <-- this is the important line - change it to anything other than the default, which is the module name ('main' in this case)