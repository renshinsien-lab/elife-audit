from django.apps import AppConfig

class AuditTrailConfig(AppConfig):
    name = "audit_trail"

    def ready(self):
        import audit_trail.signals