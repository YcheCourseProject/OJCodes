from munkres import Munkres
import numpy
import math

def get_positions(file_name):
    with open(file_name) as ifs:
        lines = ifs.readlines()
        tuple_list = map(lambda ele: map(float, ele.split()), lines)
        return tuple_list


def compute_dist(left, right):
    return math.sqrt((left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2)


def get_answer():
    passengers = get_positions('passenger.txt')
    uber_cars = get_positions('uber_car.txt')
    print 'passenger num:', len(passengers)
    print 'uber num:', len(uber_cars)
    matrix = []
    for passenger in passengers:
        tmp_matrix = []
        for uber_car in uber_cars:
            tmp_matrix.append(compute_dist(passenger, uber_car))
        matrix.append(tmp_matrix)
    print len(matrix), len(matrix[0])

    m = Munkres()
    indexes = m.compute(matrix)
    total = float(0)
    for row, column in indexes:
        value = matrix[row][column]
        total += value
        print 'P%d-U%d' % (row + 1, column + 1)
    print 'total cost: %d' % total

get_answer()