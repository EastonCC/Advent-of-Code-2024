def convert_file_to_locations(file_path):
    with open(file_path, 'r') as file:
        location_str = file.read()
        
    locations = [int(l) for l in location_str.split() if l.isdigit()]
    locations1 = locations[::2] # get even indices
    locations2 = locations[1::2]# get odd indices
    locations1 = sorted(locations1)
    locations2 = sorted(locations2)
    return locations1, locations2
                
locations1, locations2 = convert_file_to_locations('locations.txt')

def calc_similarity_score(list1, list2):
    multiplied = []
    for num in list1:
        multiplied.append(num * list2.count(num))
    return sum(multiplied)   

print(calc_similarity_score(locations1, locations2))
