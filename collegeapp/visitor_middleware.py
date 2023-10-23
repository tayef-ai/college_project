from .models import Visitor
from django.utils import timezone

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        Visitor.objects.create(timestamp=timezone.now())
        response = self.get_response(request)
        return response
