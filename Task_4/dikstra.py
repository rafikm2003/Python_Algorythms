import heapq


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







def dijkstra(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # Funkcja pomocnicza do sprawdzania sąsiadów
    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    # Znajdowanie pozycji początkowej i końcowej
    start, end = None, None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)
    
    if not start or not end:
        raise ValueError("Brak początku lub końca labiryntu.")
    
    # Inicjalizacja odległości od startu do każdego pola jako nieskończoność
    distance = {pos: float('inf') for pos in [(i, j) for i in range(rows) for j in range(cols)]}
    distance[start] = 0
    
    # Kolejka priorytetowa dla algorytmu Dijkstry
    pq = [(0, start)]
    
    while pq:
        dist, current = heapq.heappop(pq)
        
        if current == end:
            break
        
        for direction in directions:
            new_row, new_col = current[0] + direction[0], current[1] + direction[1]
            
            if is_valid_move(new_row, new_col) and grid[new_row][new_col] != 'x':
                new_dist = dist + 1  # W labiryncie, gdzie każde pole ma taką samą wagę
                
                if new_dist < distance[(new_row, new_col)]:
                    distance[(new_row, new_col)] = new_dist
                    heapq.heappush(pq, (new_dist, (new_row, new_col)))
    
    # Rekonstrukcja ścieżki
    path = []
    current = end
    while current != start:
        path.append(current)
        for direction in directions:
            new_row, new_col = current[0] - direction[0], current[1] - direction[1]
            if is_valid_move(new_row, new_col) and distance[current] == distance[(new_row, new_col)] + 1:
                current = (new_row, new_col)
                break
    path.append(start)
    path.reverse()
    
    return path


maze = load_to_2d_array('lab-9-student-bida-agh-master/labirynt_v2.txt')
found_path = dijkstra(maze)
print("Znaleziona ścieżka:")
for row, col in found_path:
    maze[row][col] = '*'

for row in maze:
    print(''.join(row))
