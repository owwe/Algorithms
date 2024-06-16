
def get_input(path = 'tinyUF.txt'):
    data = []
    with open(path,'r') as file:
        i = file.readline()
        for line in file:
            a,b = line[:-1].split(' ')
            data.append([int(a),int(b)])
    return data

def get_input_gen(path = 'tinyUF.txt'):
    with open(path,'r') as file:
        _ = file.readline()
        for line in file:
            a,b = line[:-1].split(' ')
            yield int(a),int(b)


if __name__ == "__main__":
    for a,b in get_input_gen():
        print(a,b)