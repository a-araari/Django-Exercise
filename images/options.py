from datetime import datetime, timedelta

from django.conf import settings

from .models import UploadRecord


def get_client_ip(request):
    """
    Get the client's IP Address
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_upload_count(ip_address):
    """
    Get the current upload count for the provided IP Address
    during a defined period of time.
    """
    time_window = datetime.now() - timedelta(hours=settings.UPLOAD_TIME_WINDOW)
    return UploadRecord.objects.filter(ip_address=ip_address, upload_datetime__gte=time_window).count()
