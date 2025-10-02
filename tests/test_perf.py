import pytest

def test_ping_perf(benchmark, client):
    def hit():
        return client.get("/api/ping/")
    result = benchmark(hit)
    assert result.status_code == 200
