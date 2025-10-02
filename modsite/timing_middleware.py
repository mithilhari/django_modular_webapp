import time
from typing import Callable
from django.http import HttpRequest, HttpResponse

class RequestTimingMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        start = time.perf_counter()
        response = self.get_response(request)
        elapsed_ms = (time.perf_counter() - start) * 1000
        response["X-Request-Duration-ms"] = f"{elapsed_ms:.2f}"
        return response
