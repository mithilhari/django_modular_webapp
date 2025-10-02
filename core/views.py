from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from .services import latest_notes

def home(request: HttpRequest) -> HttpResponse:
    notes = latest_notes(limit=5)
    return render(request, "index.html", {"notes": notes})

def ping(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"ok": True, "message": "pong"})
