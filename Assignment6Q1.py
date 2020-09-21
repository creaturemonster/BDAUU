import numpy

hugeNumber = float("inf")
unused = -1000

stages = 6
inventory = 4
inventoryCapacity = 15
productionCapacity = 15 - inventory

setupCost = numpy.array([unused, 120, 125, 130, 125, 120, 110])  # "unused" is for element 0,
unitCost = numpy.array([unused, 8.00, 10.00, 9.50, 9.50, 10.00, 10.00])  # which we don't use
holdingCost = numpy.array([unused, 0.50, 0.60, 0.60, 0.70, 0.75, 0.70])
shortageCost = numpy.array([unused, 35.00, 40.00, 35.00, 30.00, 25.00, 25.00])
itemDemand = numpy.array([unused, 3, 4, 5, 9, 11, 7])

minDemand = 3
maxDemand = 11

# End of input data section


f = numpy.zeros([stages + 2, inventoryCapacity + 1])
x = numpy.zeros([stages + 1, inventoryCapacity + 1], dtype=int)

for t in range(stages, 0, -1):

    for i in range(inventoryCapacity + 1):

        minProduction = max(0, maxDemand - i)

        maxProduction = min(productionCapacity, inventoryCapacity - i + minDemand)
        value = hugeNumber
        bestMove = unused  # Nothing meaningful in here yet

        for p in range(minProduction, maxProduction + 1):

            # Compute production cost
            productionCost = unitCost[t] * p
            if p > 0:
                productionCost += setupCost[t]
            inventory = inventory + p - itemDemand[t]
            productionCost += (inventory + p - itemDemand[t]) * holdingCost[t] / 2
            moveValue = productionCost
            for d in range(minDemand, maxDemand + 1):
                if (inventory + p < itemDemand[t]):
                    moveValue += (itemDemand[t] - p - inventory) * (shortageCost[t])
            if moveValue < value:
                value = moveValue
                bestMove = p

        # End of p loop

        f[t, i] = value
        x[t, i] = bestMove

        # End of i loop

# End of t loop

print("Optimal expected cost is " + str(f[1, 4]))
print("Period 1: produce " + str(x[t, 4]))
for t in range(2, stages + 1):
    print("Period " + str(t) + ":")
    sumOfxt = sum(x[t, :])
    for i in range(inventoryCapacity + 1):
        print("    If inventory=" + str(i) + ", produce " + str(x[t, i]))
        sumOfxt -= x[t, i]
        if sumOfxt <= 0:
            print("    If inventory>" + str(i) + ", produce 0")
            break
