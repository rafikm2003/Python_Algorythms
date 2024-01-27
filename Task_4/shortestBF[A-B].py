def find_shortest_path(maze):
    rows, cols = len(maze), len(maze[0])
    start, end = None, None

    # Find the start and end points
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'A':
                start = (i, j)
            elif maze[i][j] == 'B':
                end = (i, j)

    if not start or not end:
        raise ValueError("Start or end point not found in the maze")

    def dfs(current, path):
        i, j = current

        # Base case: reached the end
        if current == end:
            return path + [current]

        # Mark the current position as visited
        maze[i][j] = 'visited'

        # Explore neighbors
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor in neighbors:
            ni, nj = neighbor
            if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] != 'x' and maze[ni][nj] != 'visited':
                result = dfs(neighbor, path + [current])
                if result:
                    return result

        # Unmark the current position when backtracking
        maze[i][j] = ' '

    # Perform DFS starting from the 'A' position
    path = dfs(start, [])

    if path:
        return len(path), path
    else:
        return float('inf'), []  # No path found

def display_solved_maze(maze, path):
    for point in path:
        i, j = point
        maze[i][j] = '.'

    for row in maze:
        print(' '.join(row))

# Initialize a 2D array
def load_to_2d_array(file_path):
    two_d_array = []
# Open the file and read its contents
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Create a list for the characters in the line, excluding newline characters
            char_list = [char for char in line if char != '\n']
        
        # Append the list of characters to the 2D array
            two_d_array.append(char_list)
        return two_d_array
# Example usage:
maze = load_to_2d_array('lab-9-student-bida-agh-master/labirynt_v2.txt')

shortest_path_length, shortest_path = find_shortest_path(maze)

if shortest_path_length != float('inf'):
    print(f"The shortest path length is: {shortest_path_length}")
    display_solved_maze(maze, shortest_path)
else:
    print("No path found.")

