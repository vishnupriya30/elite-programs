def gcd(l, b):
    if l ==  0:
        return b
    elif b == 0:
        return l
    else:
        return gcd(b, l%b)
#a piece of length l and breadth b is cut into (l//g)*(b//g) equal squares
def no_of_squares(l,b):
    g = gcd(l,b)
    return (l//g) * (b//g)
print(no_of_squares(16,64))

