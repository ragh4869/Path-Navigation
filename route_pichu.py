import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        # Tuple of tuples containing moves for the point on map along with direction
        moves=((row+1,col,'D'), (row-1,col,'U'), (row,col-1,'L'), (row,col+1,'R'))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move[0:3], len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
def search(house_map):
        # Find pichu start position
        pichu_loc=[((row_i,col_i,),'') for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc,0)]
        
        visited_moves = [pichu_loc]
        
        while fringe:
            # Using BFS search method rather than DFS as it is ideal to go through all points in the level to achieve optimal solution 
            (curr_move, curr_dist)=fringe.pop(0)
            
            for move in moves(house_map, *curr_move[0]):
                if house_map[move[0]][move[1]]=="@":
                    # Return the distance and the path direction of the optimal path
                    return (curr_dist+1, curr_move[1]+move[2]) 
                else:
                    # Append the non-visited moves in the fringe
                    if move not in visited_moves:
                        fringe.append(((move[:2],curr_move[1]+move[2]), curr_dist + 1))
                if move not in visited_moves:
                    visited_moves.append(move)
        # Return -1 and empty path direction if there is no solution
        return (-1,'')


# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])
