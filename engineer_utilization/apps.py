from django.apps import AppConfig


class EngineerUtilizationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engineer_utilization'

    def ready(self):
        import engineer_utilization.signals
