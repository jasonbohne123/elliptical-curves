import math
#Pick Any zeta notated as z
z=14
#Initial sum is zero
Sum=0
#We will calculate Series up to 50,000 terms, should be equal to the infinite sum
#loop through calculating terms and summing them up
for k in range(1, 50000):
	Sum=Sum+1/(k**z)
#we will now solve for our approximation of Pi using the Zeta Function
print(((18243225*Sum)/2)**(1/14))
#for comparison will compare against pi
print(math.pi)

