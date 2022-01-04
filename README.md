### Path Navigation

##### Objective -
To find the optimal path between pichu and the goal, and return the path length and direction to the goal.

##### Initial State: 
The initial state consists of the house map with the pichu in the starting point and the goal point in its location.

##### Set of Valid States:
All the positions marked "." are set of valid states/points the pichu can move to reach the goal.

##### Successor Function:
Provides all the valid moves for the pichu, from the current coordinate, to move along with the path direction.

##### Cost Function:
The cost function computes the number of moves taken for the pichu to reach the goal. Each move has a cost of 1.

##### Goal State:
The goal state is the state when the pichu has traveled the path optimally and reached the goal, that is, "@".

##### Reason for failure of skeleton code:
In the skeletal code, the algorithm implemented is DFS search method and while implementing it, there has been no precautions taken to check if a coordinate is revisited. Once the pichu revisits the coordinate, it keeps looping with the same 2 coordinates in DFS and falls into an infinite loop.
Also, the code does not provide the actual distance and path to the goal "@".

##### Solution Implemented:
The code first takes in the system arguments and the map is sent to the solve function. It then finds the location of the pichu and records the coordinates in the fringe and the visited_moves. The visited moves list is added to eliminate the possibility of infinite loop as the pichu will not visit the same coordinate again. The code then gets the possible moves for the pichu to move to the next position. I added the path directions along with the possible coordinates, and by adding this will eliminate the need to compute the path directions of the optimal path at a later time. Along with getting the next moves, I also keep appending the positions vistied by the pichu and append their coordinates in the visited_moves list. As in the skeletal code, the output returned was a random set. This is changed with returning the optimal path distance and directions taken by the pichu to reach the goal. Finally, I used 2 search methods. I used the DFS search method first and found that for maps having multiple complete paths, the path chosen by the pichu was not optimal. Due to this, I switched to using BFS search method as it checks all the coordinates at the same depth level, leading pichu to choose the ideal path.


##### Command:
The following command can be used to run the program in the command prompt-

python route_pichu.py map1.txt 
