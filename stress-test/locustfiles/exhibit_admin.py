# from locust import HttpUser, TaskSet, task, between, constant
# import random
# import logging


# class ExhibitUserBehavior(TaskSet):
#     @task
#     def waiting_time(self):
#         with self.client.post(
#             url="/waiting-time",
#             headers={
#                 "authorization": self.access_token,
#                 "Content-Type": "application/json",
#                 "Accept": "application/json",
#                 "hogehoge": "fugafuga",
#             },
#             json={"type": "WAITING", "minutes": random.randint(1, 60)},
#             catch_response=True,
#         ) as response:
#             if response.status_code != 200:
#                 response.failure(f"Failed to create waiting time {response.text}")

#     def login(self):
#         headers = {
#             "Content-Type": "application/x-www-form-urlencoded",
#             "Accept": "application/json",
#         }
#         with self.client.post(
#             "/auth/login", data={"username": "2M", "password": "r380ocr9"}, headers=headers, catch_response=True
#         ) as response:
#             if response.status_code == 200:
#                 self.access_token = f"{response.json()['token_type']} {response.json()['access_token']}"
#             else:
#                 response.failure(f"Failed to login {response.text}")

#     def on_start(self):
#         self.login()


# class ExhibitUser(HttpUser):
#     tasks = {ExhibitUserBehavior: 1}
#     wait_time = between(1, 2)
