#!/usr/bin/env python

""" ... """

import sys, json

# courses_reqs

def scheduler_dfs(filename):

    with open(filename) as schedule_data:    
        course_catalog = json.load(schedule_data)

    # List of courses as can be performed
    sorted_schedule = []
    print(course_catalog)

    # while course_catalog != []:

    acyclic = False
    for index, course in enumerate(course_catalog): 

        name = course['name']
        prereqs = course['prerequisites']

        for prereq in prereqs:
            print(name, prereqs)
            if prereq == []:
                sorted_schedule.append(prereq)
            
        else:
            acyclic = True
            del course_catalog[index]
            sorted_schedule.append(name)

    raise RuntimeError("Error: unresolvable loop in requirements")

    for course in sorted_schedule:
        print(course)

    return sorted_schedule


json_filename = sys.argv[1] if len(sys.argv) > 1 else "../../../clever/math.json"
print(scheduler_dfs(json_filename))