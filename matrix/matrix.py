import numpy as np
class Matrix:
    def __init__(self,shape = (3,4),fill = 0):
        self.shape = shape
        if fill == 'random':
            self.matrix = [[np.round(np.random.randn(),2) for j in range(self.shape[1])] for i in range(self.shape[0])]
        else:
            self.matrix = [[fill for j in range(self.shape[1])] for i in range(self.shape[0])]

    def array(self,arr = [[1,2,4],[1,2,3]]):
        self.matrix = arr
        try:
            self.shape = (len(arr),len(arr[0]))
        except:
            self.shape = (len(arr),0)

    def __str__(self):
        o = ''
        for line in self.matrix:
            for i in line:
                o += f' {i} '
            o+='\n'
        return o
    
    def __add__(self,other):
        if isinstance(other,int) | isinstance(other,float):
            result = Matrix(shape = self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.matrix[i][j] =  self.matrix[i][j] + other
            return result
        elif  self.shape == other.shape:
            result = Matrix(shape = self.shape)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        else:
            raise Exception(f"DimError: Dimensions are wrong {self.shape} and {other.shape} do not match")
        
    def __sub__(self,other):
        if isinstance(other,int) | isinstance(other,float):
            result = Matrix(shape = self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.matrix[i][j] =  self.matrix[i][j] - other
            return result
        elif  self.shape == other.shape:
            result = Matrix(shape = self.shape)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result
        else:
            raise Exception(f"DimError: Dimensions are wrong {self.shape} and {other.shape} do not match")
    
    def __mul__(self,other):
        if isinstance(other,int) | isinstance(other,float):
            result = Matrix(shape = self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.matrix[i][j] =  self.matrix[i][j] * other
            return result
    def dot(self,other):
        if isinstance(other,int) | isinstance(other,float):
            result = Matrix(shape = self.shape)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result.matrix[i][j] =  self.matrix[i][j] * other
            return result
        elif self.shape[1] == other.shape[0]:            
            result = Matrix(shape = (self.shape[0],other.shape[1]),fill = 0)
            for i in range(self.shape[0]):
                for j in range(other.shape[1]): 
                    total = 0
                    for t in range(self.shape[1]):
                        total += self.matrix[i][t] * other.matrix[t][j]
                    result.matrix[i][j] = total
            return result
        else:
            raise ValueError (f"DimError: Dimensions are wrong {self.shape} and {other.shape} do not match")
    def eye(self,n):
        result = Matrix(shape = (n,n),fill = 0)
        for i in range(n):
            for j in range(n):
                if i == j:
                    result.matrix[i][j] = 1
        return result

if __name__ == "__main__":
    m1 = Matrix(shape = (2,4))
    m2 = Matrix(shape = (2,4))

    m3 = Matrix()
    m3.array(arr= [[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    print(m3)
    m3 += 1
    print(m3)
    eye = Matrix()
    eye.array(arr = [[1,0,0],[0,1,0],[0,0,1]])
    eye *= 2
    print(f'eye \n{eye}')
    result = m3.dot(eye)
    print(f"result \n{result}")

    