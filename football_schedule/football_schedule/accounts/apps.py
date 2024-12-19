from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'football_schedule.accounts'

    def ready(self):
        import football_schedule.accounts.signals
