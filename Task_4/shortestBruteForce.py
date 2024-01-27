def find_shortest_path(maze):
    start = find_start(maze)
    end = find_end(maze)

    if not start or not end:
        print("Error: Maze does not have a valid start or end point.")
        return

    path = dfs(maze, start, end, [])
    
    if path:
        print_path(maze, path)
    else:
        print("No path found.")

def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'A':
                return (i, j)
    return None

def find_end(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'B':
                return (i, j)
    return None

def is_valid_move(maze, row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == ' '

def dfs(maze, current, end, path):
    row, col = current
    maze[row][col] = 'visited'
    path.append((row, col))

    if current == end:
        return path

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_move(maze, new_row, new_col):
            new_path = dfs(maze, (new_row, new_col), end, path.copy())
            if new_path:
                return new_path

    return None

def print_path(maze, path):
    for row in maze:
        print(''.join(row))
    
    for row, col in path:
        maze[row][col] = '.'
    
    print("\nShortest Path:")
    for row in maze:
        print(''.join(row))


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
# Example Maze
maze = load_to_2d_array('lab-9-student-bida-agh-master/labirynt_v2.txt')

find_shortest_path(maze)

