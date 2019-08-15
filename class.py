class Vector:
    def __init__(self,d):
        """ create d-dimensional vector of zeroes"""
        self._coords = []
        for i in range(d):
            l = float(input())
            self._coords.append(l)

    def __len__(self):
        return len(self._coords)
    def __getitem__(self,k):
        return self._coords[k]

    def __setitem__ (self,j,val):
        self._coords[j] = val;

    def __add__(self,other):
        if (len(self)!=len(other)):   
            raise ValueError('dimensions must agree')
        result = Vector(len(self))   
        for i in range(len(self)):
            result[i] = self[i]+other[i]
        return result

    def __eq__(self,other):
        return self._coords == other._coords

    def __ne__(self,other):
        return not self == other

    def __str__(self):
        return ('<'+str(self._coords)[1:-1]+'>')


if __name__ == "__main__":
    v = Vector(3)
    """v[0] = 2
    v[1] = 9
    v[2] = 7"""
    print(v)
    c = Vector(3)
    #for i in range(3):
     #   input(c[i])

    print(c+v)


