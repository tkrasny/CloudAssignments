from typing import Optional
from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

queue = []
nsongs = 0

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/songs")
def read_all_songs(title: Optional[str] = None):
    if title is not None:
        lookupIndex = search_by_title(title)
        if lookupIndex is not -1:
            song = queue[lookupIndex]
            return {"song_id": song["song_id"], "title": song["title"]}
        else:
            # No matches found for given title- return blank response
            return {}

    # No filtering done- return all songs
    return queue

@app.get("/songs{song_id}")
def read_song(song_id: int):
    lookupIndex = search_by_id(song_id)
    song = queue[lookupIndex]
    return {"song_id": song["song_id"], "title": song["title"]}

@app.get("/songs{song_id}/title")
def read_song_title(song_id: int):
    lookupIndex = search_by_id(song_id)
    song = queue[lookupIndex]
    return {"title": song["title"]}

@app.put("/songs/{song_id}")
def update_song(song_id: int, title: Optional[str] = None):
    global queue
    lookupIndex = search_by_id(song_id)
    song = queue[lookupIndex]
    if title is not None:
        song["title"] = title

    return {"song_id": song["song_id"], "title": song["title"]}

@app.post("/songs")
def create_song(title: str):
    global queue
    global nsongs

    song_id = nsongs
    nsongs+=1

    song = {}
    song["song_id"] = song_id
    song["title"] = title

    queue.append(song)
    return {"song_id": song_id, "title": title}


@app.delete("/songs{song_id}", status_code=200)
def delete_song(song_id: int):
    global queue
    lookupIndex = search_by_id(song_id)
    song = queue[lookupIndex]
    queue.remove(song)

@app.delete("/songs", status_code=200)
def delete_all():
    global queue
    global nsongs
    nsongs = 0
    queue = []

def search_by_title(title):
    global queue

    lookupIndex = next((lookupIndex for lookupIndex, song in enumerate(queue) if song["title"] == title), -1)

    return lookupIndex

def search_by_id(id):
    global queue

    # lookup the ID
    lookupIndex = next((lookupIndex for lookupIndex, song in enumerate(queue) if song["song_id"] == id), -1)

    if lookupIndex is -1:
        raise HTTPException(status_code=404, detail="Song not found")
    else:
        return lookupIndex