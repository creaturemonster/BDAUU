'''
Function gives all combinations of number of flights possible that will give a
sum of 14 (since there are only 14 flights available)
l: list of numbers that can add up to 14
yet: initially an empty list
a: an empty dictionary
'''


def total(l, yet, a):
    # sum of all elements in the list - yet
    s = sum(yet)
    if s == 14:
        a[string(yet)] = 1  # if s is 14, save it in the dictionary a
        return

    elif s > 14:  # if s exceeds 14, ignore it
        return

    n = len(l)  # length of numbers in list l
    for i in range(n):
        # call the fucntion recursively with l not having the current element and yet having it
        total(l[i + 1:], yet + [l[i]], a)


'''
Function returns a string concatenating the numbers present in list l
'''


def string(l):
    s = ''
    for num in l:
        s += str(num)
    return s


'''
Function to be called first
'''


def flights(costs):
    # maximum number of 1 number of flights is 6 since 6 < 14
    # maximum number of 2 number of flights is , since 6*2 < 14
    # similarly for 6, maximum is 2, since 6*2 < 14
    # l is the list of the numbers that can add up to 14
    l = [1] * 6 + [2] * 6 + [3] * 4 + [4] * 3 + [5] * 2 + [6] * 2

    # empty dictionary
    a = {}
    # function called, dictionary a will be edited
    total(l, [], a)

    # maximum profit initialized
    max = 0
    # all combinations present in a are checked
    key = ''
    for k in a:
        p = profit(k, costs)
        if p > max:
            max = p
            key = k

    displaySchedule(key, costs)
    print("For the given data, maximum profit is: "+key)


def profit(k, costs):
    # initialize index of each number of flight.
    indexes = [0] * 6
    p = 0
    for c in k:
        i = int(c)
        # chose the highest profit first
        p += costs[i - 1][indexes[i - 1]][0]
        # increment the index, so that the second highest profit can be taken
        indexes[i - 1] += 1

    return p


def displaySchedule(k, costs):
    indexes = [0] * 6
    # List of city names
    cities = ["New York", "Los Angeles", "Miami", "Chicago", "Seattle", "Atlanta"]
    # number of flights initialised to zero for each city
    sched = {"New York": 0, "Los Angeles": 0, "Miami": 0, "Chicago": 0, "Seattle": 0, "Atlanta": 0}
    # for each character in k. the character is converted to an int
    # the index of the highest profit flight is noted and is used to access the city name
    # the number of flights taken from the city is then incremented in the dictionary sched
    for c in k:
        i = int(c)
        ind = costs[i - 1][indexes[i - 1]][1]
        sched[cities[ind - 1]] += i
        indexes[i - 1] += 1

    for city in sched:
        print(city + ": " + str(sched[city]) + " Flights.")
        print(" ")


# data saved in this way
# costi is the list of flight costs for all cities when i number of flights are taken
# each of these lists have a tuple which signifies the index of the city

costs1 = [(80, 1), (100, 2), (90, 3), (120, 4), (70, 5), (80, 6)]
costs2 = [(150, 1), (195, 2), (180, 3), (200, 4), (160, 5), (175, 6)]
costs3 = [(210, 1), (275, 2), (265, 3), (240, 4), (190, 5), (245, 6)]
costs4 = [(250, 1), (325, 2), (310, 3), (245, 4), (230, 5), (280, 6)]
costs5 = [(270, 1), (300, 2), (350, 3), (290, 4), (250, 5), (340, 6)]
costs6 = [(280, 1), (250, 2), (320, 3), (300, 4), (290, 5), (330, 6)]
# saving all these lists in the list cost
costs = [costs1,costs2,costs3,costs4,costs5,costs6]

# sort all the lists present in the list cost in decreasing order
for cost in costs:
    cost.sort(reverse=True)

flights(costs)
