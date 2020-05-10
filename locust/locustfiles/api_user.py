from locust import HttpLocust, TaskSet, between, task, seq_task


class UserBehavior(TaskSet):

    def on_start(self):
        self.token = None

        with self.client.post("/authentication",
                              {'strategy': 'local', 'email': 'jone@doe.test', 'password': '123456'}) as response:
            if response.status_code != 201:
                response.failure("Authentication failed!")
            else:
                json_body = response.json()
                self.token = json_body['accessToken']

    @seq_task(1)
    @task(1)
    def create(self):
        self.client.post("/students",
                         headers={'Authorization': 'Bearer ' + self.token},
                         data={'name': 'John Doe', 'age': 21})

    @seq_task(2)
    @task(2)
    def list(self):
        self.client.get("/students",
                        headers={'Authorization': 'Bearer ' + self.token},
                        )


class ApiUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 10.0)
    host = "http://localhost:3030"
