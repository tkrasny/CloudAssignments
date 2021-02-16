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
def read_song(song_id: Optional[int] = None, title: Optional[str] = None):
    global queue

    if song_id is None and title is None:
        #Default to printing the entire queue if no parameters are provided
        #TODO: Check on formatting here
        return queue

    #Search by title
    if title is not None:
        print("Searching by title")
        lookupIndex = search_by_title(title)

    #Search by ID
    if song_id is not None:
        print("Searching by ID")
        lookupIndex = search_by_id(song_id)


    song = queue[lookupIndex]
    #TODO: Error check this

    return {"song_id": song["song_id"], "title": song["title"]}


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


def search_by_title(title):
    global queue

    #lookup the title
    lookupIndex = next((lookupIndex for lookupIndex, song in enumerate(queue) if song["title"] == title), -1)

    if lookupIndex is -1:
        print("SONG NOT FOUND")
        raise HTTPException(status_code=404, detail="Song not found")
    else:
        return lookupIndex


def search_by_id(id):
    global queue

    # lookup the ID
    lookupIndex = next((lookupIndex for lookupIndex, song in enumerate(queue) if song["song_id"] == id), -1)

    if lookupIndex is -1:
        print("SONG NOT FOUND")
        raise HTTPException(status_code=404, detail="Song not found")
    else:
        return lookupIndex