import numpy
from binomialPoisson import *
hugeNumber = float("inf")
unused = -1000
price=numpy.array([150,200,250])
stages=10
numberOfRooms=20
meanDemand=numpy.array([5.1,3.2,1.3])
numPrices=len(price)
elements=3
#End of Input Data
# This is the highest demand we could ever possibly meet
maxSupply = numberOfRooms
for i in range(elements):
    beta = 1.0 / (1.0 + price[i])

f = numpy.zeros([stages + 2, numberOfRooms + 1])
x = numpy.zeros([stages + 1, numberOfRooms + 1], dtype=int)

# Set the value of ending up in each final state (not zero in this case)
# We are doing this as a max problem, so the terminal value is positive
for t in range(stages,0,-1):
    for i in range(numberOfRooms+1):
        value=-hugeNumber
        bestMove=0
        for p in range(numPrices):
            moveValue=0
            demandProb=poisson(meanDemand[p],i)
            for d in range(i+1):
                j=i-d
                moveValue+=demandProb[d]*(d*price[p]+f[t+1,j])
                if moveValue > value:
                        value=moveValue
                        bestMove=p
                f[t,i]=value
                x[t,i]=bestMove
# End of t loop

print("Optimal EMV is " + str(f[1, numberOfRooms]))
print("Period 1: produce " + str(price[x[t, 20]]))
for t in range(2, stages + 1):
    print("Period " + str(t) + ":")
    sumOfxt = sum(x[t, :])
    for i in range(numberOfRooms + 1):
        print("    If inventory=" + str(i) + ", price is " + str(price[x[t, i]]))
        sumOfxt -= x[t, i]
        if sumOfxt <= 0:
            print("    If inventory>" + str(i) + ", produce 0")
            break
