import sys, json
from pprint import pprint

def scheduler(course_catalog):
    with open(sys.argv[1]) as schedule_data:    
        course_catalog = json.load(schedule_data)

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