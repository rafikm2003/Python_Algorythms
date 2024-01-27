import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])
    
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, end)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == end:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1]

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if maze[neighbor[0]][neighbor[1]] == 'x':
                    continue
            else:
                # neighbor out of range
                continue

            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
            
            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))
                
    return False

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

start = (0, 0)
end = (20, 30)

path = a_star(maze, start, end)
print("Znaleziona ścieżka:")
for row, col in path:
    maze[row][col] = '*'

for row in maze:
    print(''.join(row))
