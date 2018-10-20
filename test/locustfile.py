from locust import HttpLocust, TaskSet, task

class UserTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/?p=1")

    def image(self):
        self.client.get("/?p=9")

    def text(self):
        self.client.get("/?p=11")


class WebsiteUser(HttpLocust):
    task_set = UserTasks