from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 20)
    host = 'http://jsonplaceholder.typicode.com'


    @task(100)
    def addPost(self):
        self.client.post("/posts", json={
            "userId": 1,
            "title": "test1",
            "body": "bodytest1"
        })

    @task(10)
    def getPosts(self):
        self.client.get("/posts")

    @task(5)
    def deletePost(self):
        self.client.delete("/posts/1")

    @task(4)
    def getPost2(self):
        self.client.get("/posts/2")

    @task(3)
    def putPost2(self):
        self.client.put("/posts/2", json={
            "userId": 1,
            "title": "testnewput",
            "body": "bodytestnewput"
        })

    @task(2)
    def patchPost3(self):
        self.client.patch("/posts/3", json={
            "userId": 1,
            "title": "testnewpatch",
            "body": "bodytestnewpatch"
        })

#http://localhost:8089/