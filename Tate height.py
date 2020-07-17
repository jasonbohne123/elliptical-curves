import Elliptic03,numpy
#imports essential packages

curve = Elliptic03.Curve("y**2 == x**3-2*x+2", -2, 2) #sets elliptical curve
P = Elliptic03.Point(curve, 1, 1) #sets point of infinite order
n=25 #sets how far we want to calculte height of point
error=0.001 #sets error to determine how much the value stabalizes

def stabalizer(arr):
    for x in range(0,n-1):
        if abs(arr[x+1]-arr[x])<error:
            return (x+1)
# stabalizes function that inputs array and loops through to find the first time values are within a set error

array=[]
Q=P
for x in range(1,n):
    Q+=P
    largest=float(max(abs(Q.xCoord.denominator),abs(Q.xCoord.numerator)))
    value = numpy.log(largest)/((x+1)**2)
    array.append(value)
    #Loops through n times and calculates the height of the Logarithmic height of the elliptical curve, appends to an array
    #print(value)

print("It takes",stabalizer(array),"times before the difference in the logarithmic height of the point is within", error)
