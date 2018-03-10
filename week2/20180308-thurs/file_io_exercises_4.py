import matplotlib
matplotlib.use("Agg")
import json

from matplotlib import pyplot

def get_points(file_name):
    with open(file_name, 'r') as file_handle:
        points_dict = json.load(file_handle)
    return points_dict

def get_x_coords(points_dict):
    xs = []
    for coord in points_dict['data']:
        xs.append(coord[0])
    return xs

def get_y_coords(points_dict):
    ys = []
    for coord in points_dict['data']:
        ys.append(coord[1])
    return ys

if __name__ == "__main__":
    file = input("Please enter the name of your coordinates file: ")
    
    points_dict = get_points(file)
    
    xs = get_x_coords(points_dict)
    ys = get_y_coords(points_dict)
    
    pyplot.scatter(xs, ys)
    pyplot.savefig('file_io_exercises_4.png')
    pyplot.close()