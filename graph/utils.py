
import numpy as np

def get_input(path = 'tinyUF.txt'):
    with open(path,'r') as file:
        v = file.readline()
        e = file.readline()
        vertices = [[] for i in range(v)]
        for line in file:
            a,b = line[:-1].split(' ')
            vertices[int(a)].append(int(b))
    return vertices

def get_input_gen(path = 'tinyUF.txt'):
    with open(path,'r') as file:
        _ = file.readline()
        _ = file.readline()
        for line in file:
            a,b = line[:-1].split(' ')
            yield int(a),int(b)


if __name__ == "__main__":
    for a,b in get_input_gen():
        print(a,b)