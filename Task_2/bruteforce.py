import os 
import math 

def is_point_inside_circle(point, circle_center, radius = 1):
    x, y = point
    center_x, center_y = circle_center

    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)

    return distance <= radius

def file_exists(file_name):
    return os.path.exists(file_name)

def load_2d_array_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Split each line into a list of numbers
            rows = [list(map(float, line.strip().split())) for line in lines]

            return rows
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



art_coords = load_2d_array_from_file('dane_testowe_1/pozycje_poczatkowe.txt')
num_of_steps = 1
art_file = 'dane_testowe_1/przemieszczenia_'
jedi_file = 'jedi_coords/jedi_po_kroku_'
txt = '.txt'
while num_of_steps <=20:
    curr_art_file = art_file+str(num_of_steps)+txt 
    curr_jedi_file = jedi_file+str(num_of_steps)+txt 
    if file_exists(curr_art_file):
        diff_in_cords = load_2d_array_from_file(curr_art_file)
        for i in range(0,len(art_coords)):
            art_coords[i][1]+=diff_in_cords[i][1]
            art_coords[i][2]+=diff_in_cords[i][2]
    else:
        print('fatal error: missing artifact file(s)')
        break
    if file_exists(curr_jedi_file):
        jedi_pos = load_2d_array_from_file(curr_jedi_file)
        for i in range(0,len(jedi_pos)):
            print('jedi o id'+str(jedi_pos[i][0])+' ma w swoim zasiegu pkt:')
            for j in range(0,len(art_coords)):
                point = (art_coords[j][1],art_coords[j][2])
                center = (jedi_pos[i][1],jedi_pos[i][2])
                if is_point_inside_circle(point, center):
                    print(art_coords[j][0])

    num_of_steps+= 1
