from django.apps import AppConfig


class ProcessoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'processo'

    # def ready(self):
    #     import processo.signals
        
    #     return super().ready()
