
A description of the purpose of the service, in about one paragraph.

    This API service acts as a song queue similar to those provided by most music-streaming
    services. The backend to the API is a list of song objects, where users can add songs only
    to the end of the queue. Users can also remove songs from the queue, retrieve information
    about the entirety of the queue or update songs in the queue.

Anything special that we need to know about running and testing your code.
    
    Nothing particularly noteworthy. To start the API service, run:

    uvicorn songsAPI:app --reload

    Then test via either the web portal, command line, or throughput.py.
    By default, throughput.py runs 100 calls on several URLs and outputs the
    calls per second each URL / method can handle. To run, simply run the python script.
        

A description of each of the operations in the service, and their corresponding URLs.

    GET: Retrieve song(s) from the queue
    * /                         : TODO: FILL THIS IN
    * /songs                    : Lists all songs in the queue
    * /songs/{song_id}          : Lists all attributes for a particular song
    * /songs/{song_id}/title    : Returns a particular song's title

    POST:
    * /songs                    : Creates a song with specified title

    PUT:
    * /songs/{song_id}          : Updates song title to provided value

    DELETE:
    * /songs                    : Deletes all songs
    * /songs/{song_id}          : Deletes a particular song from the queue

A summary of your throughput measurements and a discussion of what they mean.  

    Is the throughput higher or lower than what you expected?  
    Lower. My initial expectations were set by the vague understanding of APIs I was operating with-
    I pictured them as a lightning-fast interface between frontend and backend. While roughly 10 calls a
    second is not slow in "real-world" time, this seems slow for the low-stress single-client simulation
    I ran.

    What are the fundamental limits to the performance of your system?  
    For my throughput testing, it's single-threaded- that is, each API call must wait for the previous to 
    finish before the next is initiated. The performance could likely be boosted if the throughput was measured
    over the span of multiple clients.

    What does this mean if you want to run such a service at a large scale?
