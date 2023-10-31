# Part 1. Generating a starting solution by implementing a random algorithm
import random
import math

# First we need to create a city coordinates.
def generate_city_coordinates(num_cities):
    x_min, x_max = 0, 100  # example coordinates
    y_min, y_max = 0, 100
    city_coordinates = [(random.randint(x_min, x_max), random.randint(y_min, y_max)) for _ in range(num_cities)]

    return city_coordinates # so far it works fine. It generates a list of tuples

# Now we need a formula to calculate the distance between cities
def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return int(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

def create_distance_matrix(city_coordinates):
    num_cities = len(city_coordinates)
    distance_matrix = [[0] * num_cities for _ in range(num_cities)]

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            distance = calculate_distance(city_coordinates[i], city_coordinates[j])
            # Store the distance in both positions of the matrix since it's symmetric
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix
def create_random_tour(city_coordinates):
    num_cities = len(city_coordinates)
    tour = []  # Travel route

    # Create a list of cities to visit
    cities_to_visit = list(range(num_cities))
    start_city = random.choice(cities_to_visit)  # random city to start from
    tour.append(start_city)
    cities_to_visit.remove(start_city)

    while cities_to_visit:
        next_city = random.choice(cities_to_visit)  # Randomly choose the next city
        tour.append(next_city)
        cities_to_visit.remove(next_city)

    tour.append(start_city)  # Add the starting city again to close the route
    return tour

def create_greedy_tour(city_coordinates):
    num_cities = len(city_coordinates)
    tour = []  # Travel route

    # Create a list of cities to visit
    cities_to_visit = list(range(num_cities))
    start_city = random.choice(cities_to_visit)  # Randomly select a starting city
    tour.append(start_city)
    cities_to_visit.remove(start_city)

    while cities_to_visit:
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None

        for next_city in cities_to_visit:
            distance = calculate_distance(city_coordinates[current_city], city_coordinates[next_city])

            if distance < min_distance:
                min_distance = distance
                nearest_city = next_city

        if nearest_city is not None:
            tour.append(nearest_city)
            cities_to_visit.remove(nearest_city)
        else:
            # If nearest_city is None, it means all remaining cities are unreachable from the current city.
            # In this case, we break out of the loop.
            break

    tour.append(start_city)  # Add the starting city again to close the route
    return tour

# Writing formula to calculate the distance of the whole tour
def calculate_total_distance(city_coordinates, tour):
    total_distance = 0
    num_cities = len(tour)

    for i in range(num_cities - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        distance = calculate_distance(city_coordinates[from_city], city_coordinates[to_city])
        total_distance += distance

    return total_distance

# Example:
num_cities = 500
city_coordinates = generate_city_coordinates(num_cities)
tour = create_random_tour(city_coordinates)
total_distance = calculate_total_distance(city_coordinates, tour)
# print("Coordinates of the cities", city_coordinates)
# print("Starting solution using random algorithm:", tour)
# print("Total Distance, random:", total_distance)

city_coordinates2 = generate_city_coordinates(num_cities)
tour2 = create_greedy_tour(city_coordinates2)
total_distance2 = calculate_total_distance(city_coordinates2, tour2)
# print("Coordinates of the cities", city_coordinates2)
# print("Starting solution using greedy algorithm:", tour2)
# print("Total Distance, greedy:", total_distance2)
