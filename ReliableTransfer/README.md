Ryan Mosenkis and Chris Stankus

Our protocol sends 5 packets at a time, waits for acknowledgements from those packets, then sends another 5 packets, and repeats. 
It ignores duplicates and out of order chunks through the use of checks in the algorithm.


Protocol Sequence Diagram:

<img width="629" alt="image" src="https://user-images.githubusercontent.com/72368941/220288346-63fdfa77-31b1-43ab-b991-f30071a746d8.png">

Performance:

<img width="598" alt="image" src="https://user-images.githubusercontent.com/72368941/220288091-5723c147-9351-4d3d-a8e2-95cb07dfe8ad.png">


Our protocol works for all 4 sets of conditions.
