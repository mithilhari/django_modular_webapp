import pytest

@pytest.mark.e2e
def test_homepage_e2e(page, live_server):
    page.goto(live_server.url)
    assert page.title() != ""  # basic smoke
    page.wait_for_selector("text=Modular Django")
