# Generate a test case as follows: the number of objects is
# ( 500 , capacity of the bag 50, 70 )
# (1000, capacity of the bag 50, 70)
# ( 10000,capacity of the bag 50,70). Each object has a value and a weight between 1 and 10.
import random
#random.seed(1337)
# num  -  number of objects to iterate through
# k   -  capacity of the bag

# Construction method 1: sort by increasing weight
def construct1(num, k):
    v1 = [] # Creating a list of tupples to illustrate the set of objects.
    bag = [] # Creating a list of tupples to illustrate the contents of the knapsack
    for i in range(0, num):
        vekt = random.randint(1, 10)
        verdi = random.randint(1, 10)
        v1.append((vekt, verdi))

    # Phase 1:  Choose two algorithms to generate a starting solution
    # Algorithm 1:
    current_weight = 0
    current_value = 0
    v1.sort(key=lambda x: x[0], reverse=False)

    for item in v1:
        if current_weight + item[0] <= k:
            bag.append(item)
            current_weight += item[0]
            current_value += item[1]

    return current_weight, current_value, bag

# Construction method 2: sort by descending weight
def construct2(num, k):
    v1 = []  # Creating a list of tupples to illustrate the set of objects.
    bag = []  # Creating a list of tupples to illustrate the contents of the knapsack
    for i in range(num):
        vekt = random.randint(1, 10)
        verdi = random.randint(1, 10)
        v1.append((vekt, verdi))

    current_weight = 0
    current_value = 0
    v1.sort(key=lambda x: x[0], reverse=True)

    for item in v1:
        if current_weight + item[0] <= k:
            bag.append(item)
            current_weight += item[0]
            current_value += item[1]
    return current_weight, current_value, bag

# Optimization algorithm 1: Local Search: Greedy Improvement method Version-1
def opt_vers1(num, k, construction):
    bag = construction[2] # Get the items from the chosen construction method
    v1 = [] # all items existing in the case(500, 1000 or 10 000)
    # Creating all items which are to iterated. Putting them in the item list
    for i in range(0, num):
        vekt = random.randint(1, 10)
        verdi = random.randint(1, 10)
        v1.append((vekt, verdi))
    # Checking if the items already in the knapsack are in the all items list and removing them
    for i in bag:
        if i in v1:
            v1.remove(i)

    # Now is the real optimization
    opt_value = construction[1] # Fetching the starting value
    opt_weight = construction[0]
    better = True
    while better:
        better = False
        r_bag = random.randint(0, len(bag)-1) # select random item from the bag
        r_v1 = random.randint(0, len(v1)-1) # select random item from the item list
        bag_item_initial = bag[r_bag]
        v1_item_initial = v1[r_v1]
        bag[r_bag], v1[r_v1] = v1[r_v1], bag[r_bag] # exchanging their places
        # Lets calculate the new value and weight of the bag
        weight_new = sum(i[0] for i in bag)
        value_new = sum(i[1] for i in bag)
        if weight_new > k or value_new < opt_value:
            bag[r_bag], v1[r_v1] = bag_item_initial, v1_item_initial # reversing the swap
            continue
        # If the total weight of the bag is above the capacity or the new values
        # is less then the previous value. If so, go to the start and reverse the swap
        opt_value = value_new
        opt_weight = weight_new
        better = True
    return (opt_weight, opt_value, len(bag))

print("\nVersion 1 (capacity, value, number of items in the bag)")
print("Sort by increasing weight" + str(opt_vers1(10000, 50, construct1(10000, 70))))
print("Sort by decreasing weight" + str(opt_vers1(10000, 50, construct2(10000, 70))))

def opt_vers3(num, k, construction):
    bag = construction[2] # Get the items from the chosen construction method
    v1 = [] # all items existing in the case(500, 1000 or 10 000)
    # Creating all items which are to iterated. Putting them in the item list
    for i in range(0, num):
        vekt = random.randint(1, 10)
        verdi = random.randint(1, 10)
        v1.append((vekt, verdi))
    # Checking if the items already in the knapsack are in the all items list and removing them
    for i in bag:
        if i in v1:
            v1.remove(i)

    # Now is the real optimization
    opt_value = construction[1] # Fetching the starting value
    opt_weight = construction[0]
    better = True
    while better:
        better = False
        r_bag = random.randint(0, len(bag)-1) # select random item from the bag
        r_v1 = random.randint(0, len(v1)-1) # select random item from the item list
        bag_item_initial = bag[r_bag]
        v1_item_initial = v1[r_v1]
        bag[r_bag], v1[r_v1] = v1[r_v1], bag[r_bag] # exchanging their places
        # Lets calculate the new value and weight of the bag
        weight_new = sum(i[0] for i in bag)
        value_new = sum(i[1] for i in bag)

        if value_new > opt_value:
            if weight_new > k: # If there is a problem with the weight, we remove the lighest item
                while weight_new > k:  # Removing the lightest item in the bag
                    minst_vekt = min(bag, key=lambda item: item[0])
                    bag.remove(minst_vekt)
                    # Recalculating the weight and value
                    weight_new = sum(i[0] for i in bag)
                    value_new = sum(i[1] for i in bag)
                if value_new > opt_value:
                    opt_weight = weight_new
                    opt_value = value_new
                    better = True
            else: # Then there is no problem with the weight and we accept the changes
                opt_weight = weight_new
                opt_value = value_new
                better = True
        else: # Reversing the swap if the new value isnt better
            bag[r_bag], v1[r_v1] = bag_item_initial, v1_item_initial

    return (opt_weight, opt_value, len(bag))

print("\nVersion 3 (capacity, value, number of items in the bag)")
print("Sort by increasing weight" + str(opt_vers3(10000, 50, construct1(10000, 70))))
print("Sort by decreasing weight" + str(opt_vers3(10000, 50, construct2(10000, 70))))


















# Optimization algorithm 2:
