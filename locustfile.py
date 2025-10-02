from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def view_home(self):
        self.client.get("/")

    @task
    def api_ping(self):
        self.client.get("/api/ping/")
