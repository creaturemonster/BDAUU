import numpy
from binomialPoisson import *
hugeNumber = float("inf")
unused = -1000
stages=12
chanceFailure=0.07
inventoryCapacity=40
holdingCost=0.50
supplyParts=10
internalCost=0.004
orderCost=200
overheadCost=50
salvageValue=180
opportunityCost=450
startingInventory=13
partsNeeded=numpy.array([unused,10,20,30,40,50,60,70,80,90,100,110,120])
maxCapacity=53

#End of input data
beta = 1 / (1 + internalCost)

# Precomputes probability distributions so that
# failureProb[i,k] is the chance that if you have i machines, k will fail
failureProb = numpy.zeros([maxCapacity + 1, maxCapacity + 1])
for i in range(maxCapacity + 1):
    failureProb[i, 0:i + 1] = binomial(i, chanceFailure)
f = numpy.zeros([stages + 2, maxCapacity + 1])
x = numpy.zeros([stages + 1, maxCapacity + 1], dtype=int)

# We do this as a cost problem, so salvage value is negative
for i in range(maxCapacity + 1):
    f[stages + 1][i] = -salvageValue * i

for t in range(stages, 0, -1):

    for i in range(maxCapacity + 1):

        value = hugeNumber
        maxPurchase = maxCapacity - i

        for d in range(maxPurchase + 1):

            moveValue = d * orderCost

            for e in range(i + 1):  # Here, e is number of failures
                working = i - e
                machinesShort = max(0, partsNeeded[t] - working)
                shortageCharge = opportunityCost * machinesShort
                j = working + d
                moveValue += failureProb[i, e] * (shortageCharge + beta * f[t + 1, j])

            if moveValue < value:
                value = moveValue
                bestMove = d

        # End of d loop

        f[t, i] = value
        x[t, i] = bestMove

        # End of i loop

# End of t loop

print("Optimal cost is " + str(f[1, startingInventory]))
print("Stage 1: purchase " + str(x[1, startingInventory]) + " machines")
for t in range(2, stages + 1):
    print("At stage " + str(t) + " : ")
    for i in range(inventoryCapacity + 1):
        print("    if have " + str(i) + " machines, purchase " +
              str(x[t, i]))
