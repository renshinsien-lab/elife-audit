from .models import AuditTrail

def verify_chain():
    logs = AuditTrail.objects.order_by("id")
    prev = ""
    for log in logs:
        if log.previous_hash != prev:
            return False
        if log.calculate_hash() != log.hash:
            return False
        prev = log.hash
    return True