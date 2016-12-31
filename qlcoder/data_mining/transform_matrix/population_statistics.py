import numpy as np

if __name__ == '__main__':
    pop_vec = [16389723, 10262186, 20593430, 71685839, 49425543, 88979305, 8060519, 68538709, 33484131, 23071690,
               41755874, 26457769, 36884039, 56493891, 33397663, 42181417, 89855501, 90028072, 52745625, 61911446,
               43970320, 26994017, 76207174, 33571308, 43626674, 34462115, 24052594, 2837769, 5284525, 5970133,
               20802249]

    transition_matrix = [[0] * 31] * 31

    training_arr = np.loadtxt('population_migration.csv', str, '#', ',')
    for ele in training_arr:
        row_index, col_index = int(ele[1]), int(ele[2])
        transition_matrix[row_index][col_index] += 1

    for row_idx in xrange(31):
        inter_res = reduce(lambda x, y: x + y, transition_matrix[row_idx], 0.0)
        transition_matrix[row_idx] = map(lambda x: x / inter_res, transition_matrix[row_idx])

    print len(transition_matrix)

    res = pop_vec
    for i in xrange(5):
        res = np.dot(res, transition_matrix)

    print ','.join(map(str, res))
