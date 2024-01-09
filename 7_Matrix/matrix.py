import numpy as np
class Matrix():
    def __init__(self, listx):
        self.matrix=listx

    def Zeromatrix(self):
        a=self.matrix[0]
        b=self.matrix[1]
        if len(a) > len(b):
            if len(a[0]) > len(b[0]):
                return np.zeros((len(a), len(a[0])))
            if len(a[0]) < len(b[0]):
                return np.zeros((len(a), len(b[0])))
        if len(a) < len(b):
            if len(a[0]) < len(b[0]):
                return np.zeros((len(b), len(b[0])))
            if len(a[0]) > len(b[0]):
                return np.zeros((len(b), len(a[0])))
        if len(a) == len(b):
            return np.zeros((len(a), len(a[0])))
        return



    def Summatrix(self):
        a = self.matrix[0]
        b = self.matrix[1]
        Z= self.Zeromatrix()


        for i in range(len(a)):
            for l in range(len(a[0])):
                Z[i][l] = a[i][l]+b[i][l]
        for r in Z:
            print(r)

    def Minusmatrix(self):
        a = self.matrix[0]
        b = self.matrix[1]
        Z= self.Zeromatrix()

        for i in range(len(a)):
            for l in range(len(a[0])):
                Z[i][l] = a[i][l]-b[i][l]
        for r in Z:
            print(r)
    def Multi_2(self):
        a=self.matrix[0]
        Z = self.Zeromatrix()
        for i in range(len(a)):
            for j in range(len(a)):
                Z[i][j]=a[i][j] * 2
        for r in Z:
            print(r)
    def Multimatrix(self):
        a = self.matrix[0]
        b = self.matrix[1]
        length = len(a)
        result_matrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    result_matrix[i][j] += a[i][k] * b[k][j]
        print(result_matrix)



    def Transpose(self):
        a=self.matrix[0]
        Z=self.Zeromatrix()
        for i in range(len(a)):
            for l in range(len(a[0])):
                Z[l][i]= a[i][l]
        for r in Z:
            print(r)


list1=[[[2,4,5],
    [6,5,7],
    [9,3,1]],

    [[3,5,9],
   [4,6,7],
     [2,1,1]]]


matrix0=Matrix(list1)
# print(matrix0.Zeromatrix())


matrix0.Summatrix()
matrix0.Minusmatrix()
matrix0.Multimatrix()
matrix0.Multi_2()
matrix0.Transpose()
try:
    list1=[[[2,4],[6,5]],[[3,5,9],[4,6,7],[2,1,1]]]
    matrix0=Matrix(list1)
    matrix0.Summatrix()
except IndexError as ex:
    print(ex, file=sys.stderr)
    print("Матриці повинні мати однакову кількість строк та рядків!!", file=sys.stderr)



