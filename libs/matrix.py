import sys

class Matrix():
    def __init__(self,mass):
        self.mass = mass
        self.rows = mass.__len__()
        try:
            self.cols = mass[0].__len__()
        except AttributeError:
            print mass
            print('Error!. Only two dimension matrix!')
            sys.exit(1)
        for i in range(0, self.rows):
            if mass[i].__len__() <> self.cols:
                print mass
                print('Error!. Only matrix!')
                sys.exit(2)

    def __str__(self):
        return_string = ''
        for i in range(0,self.rows):
            for j in range(0,self.cols):
                return_string += str(self.mass[i][j]) + ' '
            if (i <> self.rows-1):
                return_string += '\n'
        return return_string        
   
    def __mul__(self,a):
        if self.cols <> a.rows:
            print('Error!. Matrix with other dim!')
            sys.exit(3)
        new_Mass = [0] * self.rows
        for i in range(0, self.rows):
            new_Mass[i] = [0] * a.cols
        for i in range (0,self.rows):
            for k in range (0,a.cols):
                for j in range(self.cols):
                    new_Mass[i][k] += self.mass[i][j] * a.mass[j][k]
        print new_Mass
        return Matrix(new_Mass)
if __name__ == '__main__':
    sys.exit(0)
    b = Matrix([[1,1,1],[1,1,1],[2,1,1]])
