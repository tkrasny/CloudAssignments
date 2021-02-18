
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

    GET:

    POST:

    PUT:

    DELETE:

A summary of your throughput measurements and a discussion of what they mean.  

    Is the throughput higher or lower than what you expected?  

    What are the fundamental limits to the performance of your system?  

    What does this mean if you want to run such a service at a large scale?