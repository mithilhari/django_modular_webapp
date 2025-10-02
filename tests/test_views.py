import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_view(client):
    resp = client.get(reverse("home"))
    assert resp.status_code == 200
    assert b"Modular Django" in resp.content

def test_ping_api(client):
    resp = client.get("/api/ping/")
    assert resp.status_code == 200
    assert resp.json().get("ok") is True
