## General Strategy

As I worked through this solution, I saw I would need to loop over every course in a work list (the ```course_reqs``` list) and find the courses that could be added to a results list (the ```sorted_schedule``` list).

Once added, the course would be deleted from the work list and I would repeat the loop over the remaining courses in the work list while there were still courses remaining. Courses with no prerequisites would be the first items added to the ```sorted_schedule``` list. 

I decided to keep the main while loop in the ```scheduler``` function and separate out the logic determining whether a course's prerequisites were all present into the ```add_ready_courses``` function. Within ```add_ready_courses```, we loop over the courses and use set math to find if a course can be added to the sorted schedule. The loop continues until there are no more courses remaining, or until we've looped over all the courses but are unable to add a course to the ```sorted_schedule```.       

## Functions
```scheduler``` is the main function -- it loads json data and creates a ```courses_reqs``` list of courses and their requirements. While there are courses in the ```courses_reqs``` list, each course will be processed by the ```add_ready_courses``` function, explained below. If the requirements of a course are present in ```sorted_schedule```, the course name will be appended to ```sorted_schedule```. 

```add_ready_courses``` checks if the prerequisites of a course are present in sorted_schedule using set math (is a set of prerequisites already in, or a subset of ```sorted_schedule```?). If so, that means the course can be added to sorted_schedule. Once added, the course is deleted from the ```courses_reqs``` list so we don't end up checking it again, and we exit the function and hop back into the while loop in ```scheduler```.  

If we have checked every course in the ```courses_reqs``` list but are unable to add a course to ```sorted_schedule```, that means that the prerequisites in ```sorted_schedule``` do not match the dependencies of the remaining courses in ```courses_reqs```. Instead of getting stuck in an infinite loop, we raise an error.

If all the courses in ```courses_reqs``` have been added to ```sorted_schedule``` and ```courses_reqs``` is empty, the courses in ```sorted_schedule``` will print the results, with each course on a new line, like so:

```
Algebra 1
Geometry
Algebra 2
Pre Calculus
```

or:

```
Calculus
Scientific Thinking
Differential Equations
Intro to Physics
Relativity
```
## Running the Script

Run scheduler on a json file, such as the ```physics.json``` or ```math.json``` files. 
(Note: the json files be properly formed, with each object having ```name``` and ```prerequisite``` keys.) 

```./scheduler physics.json```

If you encounter a ```-bash: ./scheduler: Permission denied``` error, change the file permissions using:
 ```chmod a+x [filename]```. 

```chmod a+x scheduler`` changes the permissions for all users and turns on executable permissions for all users.  

## Performance Analysis

The runtime of this approach can be improved -- we are looping over the input data twice using a while loop and a for loop nested inside the while loop, so we are looking at quadratic runtime. However, within the for loop we are also creating a set and checking if every course in the prereqs subset is present in ```sorted_schedule```, and at best this will be O(n) as we're checking every item in the course_reqs list. 

 Runtime is O(n^2) + O(n), which can be reduced to O(n^2).