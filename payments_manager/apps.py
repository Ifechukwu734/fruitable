from django.apps import AppConfig


class PaymentsManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments_manager'

    def ready(self):
        import payments_manager.signals
