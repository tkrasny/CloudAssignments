
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

    I ran 3 trial groups, of 50, 500, and 1000 consequetive requests for the following 5 requests:
    * GET (no songs populated)
    * POST
    * PUT
    * GET (songs populated)
    * DELETE

    For each, the average requests / second for the 3 trials was:
    * GET: 9.87
    * POST: 10.85
    * PUT: 8.96019983968
    * GET: 9.62308487317
    * DELETE: 10.6277706749

    Is the throughput higher or lower than what you expected?  
        Lower. My initial expectations were set by the vague understanding of APIs I was operating with-
        I pictured them as a lightning-fast interface between frontend and backend. While roughly 10 calls a
        second is not slow in "real-world" time, this seems slow for the low-stress single-client simulation
        I ran.

    What are the fundamental limits to the performance of your system?  
        For my throughput testing, it's single-threaded- that is, each API call must wait for the previous to 
        finish before the next is initiated. The performance could likely be boosted if the throughput was measured
        over the span of multiple clients.

        Additionally, the storage of data is quite poor for scalability (a locally-stored list of dictionaries).
        This is not a particularly robust or safe way of storing data, as after each session it is lost.

    What does this mean if you want to run such a service at a large scale?
        For the first issue mentioned, running the server over some sort of distributed system such as Condor would
        swiftly and concisely address this issue. Granted, this might mean the server hosting the fastAPI might need an
        upgrade as well, however this would remove this bottleneck.

        Secondly, tieing the API to an actual backend database or similar would resolve the issue of data persistence
        and scalability. Granted, adding an extra layer of communication could slow turnaround times slightly, but the benefit
        of enhanced scalability likely outweighs this drawback.
    