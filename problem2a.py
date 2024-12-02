def convert_file_to_reports(file_path):
    with open(file_path, 'r') as file:
        reports_list = file.read().splitlines() 
        
    return [list(map(int, group.split())) for group in reports_list]
                
reports = convert_file_to_reports('reports.txt')

def check_safe(report):
    adjacent_in_limits = True
    list_in_dec = False
    if (all(i < j for i, j in zip(report, report[1:]))) or all(i >= j for i, j in zip(report, report[1:])):
        list_in_dec = True
    
    for x in range(len(report) - 1):
        if not(abs(report[x] - report[x + 1]) <= 3 and abs(report[x] - report[x + 1]) >= 1):
            adjacent_in_limits = False

    return (list_in_dec and adjacent_in_limits)

def count_safe(reports):
    count = 0
    for report in reports:
        if check_safe(report):
            count += 1
    return count

print(count_safe(reports))
