from fastapi.testclient import TestClient
from songsAPI import app
import time

client = TestClient(app)

def test_getsongs():
    client.get("/songs")

def test_post():
    client.post("/songs?title=test")

def test_put(index):
    client.put(f"/songs/{index}?title=testUpdate")

def test_delete(index):
    client.delete(f"/songs/{index}")

if __name__ == "__main__":
    start_time = time.time()
    trials = [50, 500, 1000]
    for trialLen in trials:
        for i in range(trialLen):
            test_getsongs()
        end_time = time.time()
        print(f"calls per second on get /songs (empty): {trialLen / (end_time - start_time)}")

        start_time = time.time()
        for i in range(trialLen):
            test_post()
        end_time = time.time()
        print(f"calls per second on post /songs : {trialLen / (end_time - start_time)}")

        start_time = time.time()
        for i in range(trialLen):
            test_put(i)
        end_time = time.time()
        print(f"calls per second on put /songs/song_id : {trialLen / (end_time - start_time)}")

        start_time = time.time()
        for i in range(trialLen):
            test_getsongs()
        end_time = time.time()
        print(f"calls per second on get /songs (populated): {trialLen / (end_time - start_time)}")

        start_time = time.time()
        for i in range(trialLen):
            test_delete(i)
        end_time = time.time()
        print(f"calls per second on delete /songs/song_id : {trialLen / (end_time - start_time)}")