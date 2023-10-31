from oblig2_tsp_starting_solutions import *
random.seed(1234)
def optimize_tour(city_coordinates, initial_tour, max_iterations): # Max iterations here is giving a stop criterion
    current_tour = initial_tour
    current_distance = calculate_total_distance(city_coordinates, current_tour)
    best_tour = current_tour
    best_distance = current_distance

    for _ in range(max_iterations):
        # Choose two random cities to swap
        city1, city2 = random.sample(current_tour[1:-1], 2)
        new_tour = current_tour.copy() # creating a new tour just to check if the distance improves (reduces) or not
        new_tour[new_tour.index(city1)], new_tour[new_tour.index(city2)] = city2, city1 # Swap the two cities
        new_distance = calculate_total_distance(city_coordinates, new_tour)

        # If the new tour is better, accept it; otherwise, keep the previous tour
        if new_distance < current_distance:
            current_tour = new_tour
            current_distance = new_distance

            if new_distance < best_distance: # if the new distance is better, accept it
                best_tour = new_tour
                best_distance = new_distance

    return best_tour, best_distance

# --------- Here comes the testing part ----------
# Choose the number of cities
num_cities = int(input("How many cities? "))

# Choose the number of iterations
max_iterations = int(input("How many iterations? "))

city_coordinates = generate_city_coordinates(num_cities)

# Choose a greedy or random starting solution
starting_solution = input("Random or greedy starting solution? ")
if starting_solution == "random": initial_tour = create_random_tour(city_coordinates)
elif starting_solution == "greedy": initial_tour = create_greedy_tour(city_coordinates)

# Calculate the initial distance of the starting tour
initial_distance = calculate_total_distance(city_coordinates, initial_tour)

#print("Initial Tour:", initial_tour)
print(f"\nInitial Distance with {num_cities} cities:", initial_distance)

# Optimize the initial tour
optimized_tour, optimized_distance = optimize_tour(city_coordinates, initial_tour, max_iterations)
#print("\nOptimized Tour:", optimized_tour)
print(f"Optimized {starting_solution} starting solution with {num_cities} cities after {max_iterations} iterations:", optimized_distance)
print(f"Reduction in cost ", optimized_distance-initial_distance)

