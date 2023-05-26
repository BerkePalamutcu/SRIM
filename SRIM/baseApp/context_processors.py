from baseApp.models import Status
from django.core.exceptions import ObjectDoesNotExist


def navbar(self):
    try:
        # Do not change this. If you try to retrive more data than one it may break the application!
        status_report = Status.objects.get(pk=1)
    except ObjectDoesNotExist:
        status_report = None
    return {
        'status_report': status_report,
    }
