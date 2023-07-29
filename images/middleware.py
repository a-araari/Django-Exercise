from django.conf import settings
from django.core.exceptions import PermissionDenied
from .options import get_upload_count, get_client_ip


# 403 Forbidden error will be returned if the user already
# uploaded more than `settings.UPLOAD_LIMIT_VIEW_NAME`
# TODO: make a separate View for uploading images and and change
#       the value of `settings.UPLOAD_LIMIT_VIEW_NAME` to that view
#       so that is doesn't overlap with other POST requests on the
#       home page.
class UploadLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        if request.method == 'POST' and request.path == settings.UPLOAD_LIMIT_VIEW_NAME:
            ip_address = get_client_ip(request)
            upload_count = get_upload_count(ip_address)

            if upload_count >= settings.UPLOAD_LIMIT_MAX_UPLOADS_ALLOWED:
                raise PermissionDenied("You have reached the upload limit.")

        response = self.get_response(request)
        return response
