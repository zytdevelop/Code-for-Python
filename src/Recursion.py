a = 'A'
b = 'B'
c = 'C'

def Hano(a, b, c, n):
    if n == 1:
        print("{}-->{}".format(a,c))
        return None
    if n == 2:
        print("{}-->{}".format(a,c))
        print("{}-->{}".format(a,b))
        print("{}-->{}".format(b,c))
        return None
    
    Hano(a, c, b, n-1)
    print("{}-->{}".format(a,c))
    Hano(b, a, c, n-1)
