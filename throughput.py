from fastapi.testclient import TestClient
from songsAPI import app
import time

client = TestClient(app)

def test_rest_songsAPI():
    response = client.get("/")

if __name__ == "__main__":
    start_time = time.time()
    for i in range(100):
        test_rest_songsAPI()
    end_time = time.time()

    print(f"total time elapsed for 100 calls: {end_time-start_time}")
    print(f"calls per second on get / : {100 / (end_time-start_time)}")

