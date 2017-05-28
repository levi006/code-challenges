#!/usr/bin/env python

""" ... """

import sys, json

# courses_reqs

def add_ready_courses(course_catalog, sorted_schedule):
    """ ... """

    for idx, course in enumerate(course_catalog):
        prereqs = course['prerequisites']
        name = course['name']

        # if prereqs == [] or set(prereqs).issubset(sorted_schedule):
        if set(prereqs).issubset(sorted_schedule):
            sorted_schedule.append(name)
            # NOW CAN DELETE THIS FROM CATALOG
            del course_catalog[idx]
            return

    # Oh no, went through entire catalog and nothing could
    # be resolved

    raise RuntimeError("Error: unresolvable loop in requirements")

def scheduler(filename):
    """ ... """

    with open(filename) as schedule_data:    
        course_catalog = json.load(schedule_data)

    # List of courses as can  be performed
    sorted_schedule = []

    #

    while course_catalog != []:
        add_ready_courses(course_catalog, sorted_schedule)
        # print "re-looping"

    for course in sorted_schedule:
        print(course)

    return sorted_schedule

json_filename = sys.argv[1] if len(sys.argv) > 1 else "../../../clever/math.json"
scheduler(json_filename)