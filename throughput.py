from fastapi.testclient import TestClient
from songsAPI import app
import time

client = TestClient(app)

def test_getroot():
    client.get("/")

def test_getsongs():
    client.get("/songs")

def test_post():
    client.post("/songs?title=test")

if __name__ == "__main__":
    start_time = time.time()
    for i in range(100):
        test_getroot()
    end_time = time.time()
    print(f"calls per second on get / : {100 / (end_time - start_time)}")

    start_time = time.time()
    for i in range(100):
        test_getsongs()
    end_time = time.time()
    print(f"calls per second on get /songs : {100 / (end_time - start_time)}")

    start_time = time.time()
    for i in range(100):
        test_post()
    end_time = time.time()
    print(f"calls per second on post /songs : {100 / (end_time - start_time)}")

