import time
start=time.time()

def modInverse(a, prime):
    a = a % prime
    for x in range(1, prime):
        if ((a * x) % prime == 1):
            return x
    return -1
#Determines the Inverses for 1 up to p-1 for each Prime P

def returnInverses(n, prime):
    newlist=[]
    for i in range(1, n + 1):
        q=modInverse(i, prime)
        if i>=q:
            newlist.append(modInverse(i, prime))
            if i>q:
                newlist.append (i)
    newlist=' '.join(str(x) for x in newlist)
    return newlist
# Collects Inverse Pairs and stores in an array, removes double pairs

f=open('Primesupto1000.txt', 'r')
for line in f:
    list = ([elt.strip() for elt in line.split(',')])
list=map(int,list)
#Opens the File, splits commas and converts strings to Integers

for n in list:
    with open(str(n)+'.txt', 'w') as newfile:  
        newfile.write(returnInverses(n-1,n))
    #print(newfile)
    #print("MOD",n)
    #print(returnInverses(n-1,n))
#Iterate Through each prime in our inputted List and saves Inverses in a file

end=time.time()
print(end-start)
