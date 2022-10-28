from locust import HttpUser, TaskSet, between, task


class GeneralUserBehavior(TaskSet):
    @task
    def exhibit(self):
        self.client.get("/exhibit")

    @task
    def prize(self):
        self.client.get("/prize")


class GeneralUser(HttpUser):
    tasks = {GeneralUserBehavior: 1}
    wait_time = between(0, 5)
