import sys, json
from pprint import pprint

def scheduler(course_catalog):
    with open(sys.argv[1]) as data_file:    
        course_catalog = json.load(data_file)

    sorted_schedule = []

    for course in course_catalog:
        prereqs = course['prerequisites']
        name = course['name']

        if prereqs == []:
            sorted_schedule.append(name)

        elif set(prereqs).issubset(sorted_schedule):
            sorted_schedule.append(name)    

    for course in sorted_schedule:
        print(course)

    return sorted_schedule

(scheduler(sys.argv[1]))

    # for course in course_catalog:

    #     prereqs = course['prerequisites']
    #     name = course['name']

    #     if prereqs == []:
    #         satisfies[name] = []     
        
    #     else:

    #         for prereq in prereqs:

    #             if prereq not in satisfies:
    #                 satisfies[prereq] = [name]

    #             else:
    #                 satisfies[prereq].append(name)

    # pprint(satisfies)

    # n_deps = {}

    # for course in course_catalog:
    #     n_deps[course['name']] = len(course['prerequisites'])

    # pprint(n_deps)
