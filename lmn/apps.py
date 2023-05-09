from django.apps import AppConfig


class LmnConfig(AppConfig):
    name = 'lmn'

    def ready(self):
        from lmn.apis.ticketmaster_api import renew_data
        renew_data()
