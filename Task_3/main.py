def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = [list(map(float, line.strip().split()[1:])) for line in lines]
    return data

def is_valid_point(x, y):
    return 0 <= x <= 1 and 0 <= y <= 1

def find_optimal_locations_bruteforce(existing_locations, step=0.01):
    optimal_locations = []
    min_cannibalism = float('inf')

    for x in range(0, 101, int(step * 100)):
        for y in range(0, 101, int(step * 100)):
            x /= 100
            y /= 100

            if is_valid_point(x, y):
                cannibalism = sum(
                    distance(x, y, x_existing, y_existing) for x_existing, y_existing in existing_locations
                )

                if cannibalism < min_cannibalism:
                    min_cannibalism = cannibalism
                    optimal_locations = [(x, y)]
                elif cannibalism == min_cannibalism:
                    optimal_locations.append((x, y))

    return optimal_locations, min_cannibalism

file_path = 'dane.txt'
existing_locations = read_data(file_path)

optimal_locations_bruteforce, min_cannibalism_bruteforce = find_optimal_locations_bruteforce(existing_locations)

print(f"Optymalna lokalizacja): {optimal_locations_bruteforce}")
print(f"Minimalny wewnętrzny kanibalizm (brute force): {min_cannibalism_bruteforce}")
