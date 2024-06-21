
def selection_sort(l):
    for i in range(len(l)):
        min_ = 10e6
        min_index = None
        for j in range(i+1,len(l)):
            if l[j] < min_:
                min_ = l[j]
                min_index = j
        if min_< l[i]:
            l[i],l[min_index] = l[min_index],l[i]
            #print(l)

def insertion_sort(l):
    for i in range(len(l)-1):
        for j in range(i+1,0,-1):
            if l[j] < l[j - 1]:
                l[j],l[j-1] = l[j-1],l[j]
                #print(l)
            else:
                break


import random
def shuffle(l):
    for i in range(len(l)):
        r = random.randint(0,i+1)
        l[r],l[i] = l[i],l[r]
    print(l)

if __name__ == '__main__':
    # p = [1,3,5,6,8,9,0,1,22,11]
    # p = [1,34,11,10,9,8,7,6,5,4,3,2,1]
    p = [7,10,5,3,8,4,2,9,6,1]
    selection_sort(p)
    print(p)


