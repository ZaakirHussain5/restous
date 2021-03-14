from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals
        from api.schedulers import apjobs
        apjobs.start()
