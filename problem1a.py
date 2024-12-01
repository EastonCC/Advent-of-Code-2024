# Problem 1a and 1b completed in ~20 minutes

def convert_file_to_locations(file_path):
    with open(file_path, 'r') as file:
        location_str = file.read()
        
    locations = [int(l) for l in location_str.split() if l.isdigit()]
    locations1 = locations[::2]  # get even indices
    locations2 = locations[1::2] # get odd indices
    locations1 = sorted(locations1)
    locations2 = sorted(locations2)
    return locations1, locations2
                
locations1, locations2 = convert_file_to_locations('locations.txt') # locations.txt, given input from advent of code containing two tab separated columns of numbers

def abs_sum_lists(list1, list2):
    return (sum([abs(int(x) - int(y)) for x, y in zip(locations1, locations2)]))

print(abs_sum_lists(locations1, locations2))
