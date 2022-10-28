from locust import HttpUser, TaskSet, between, task


class AdminBehavior(TaskSet):
    @task
    def admin(self):
        self.client.get("/django/admin")


class Admin(HttpUser):
    tasks = {AdminBehavior: 1}
    wait_time = between(3, 30)
