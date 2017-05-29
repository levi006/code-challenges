## Design Notes

When writing this solution, I separated out what would become the ```add_when_ready``` function from the rest of the solution. The main scheduler function loads the json data files as a list and checks if the list is empty. If there are course dictionaries in the list, the first step was to check if there were any courses with no prerequisites; these would be the first items added to the ```sorted_schedule``` list and removed from the ```courses_reqs``` list. 

Moving into courses with prerequisites, I needed to check if each course prerequisite was already present in ```sorted_schedule```. Put another way, it seemed like a natural set math problem -- was the group of prereqs already in ```sorted_schedule```?  

```scheduler``` is the main function -- it loads json data and creates a ```courses_reqs``` list of courses and their requirements. While there are courses in the courses_reqs list, each course will be processed by the add_ready_courses function. If the requirements of a course are present in sorted_schedule, the course name will be appended to sorted_schedule. If all the courses in the courses_reqs list have been added to sorted_schedule and courses_reqs is empty, the courses in sorted_schedule will print out, each course on a new line. 

```add_ready_courses```: checks if the prerequisites of a course are present in ```sorted_schedule``` using set math. If so, that means the course can be added to sorted_schedule. Once added, the course is deleted from the courses_reqs list so we don't end up checking it again, and we exit the function and hop back into the while loop in scheduler().  

If we have checked every course in the courses_reqs list but are unable to add a course to sorted_schedule, that means that the prerequisites in sorted_schedule do not match the dependencies of the remaining courses in courses_reqs list. Instead of getting stuck in an infinite loop, we raise an error. 


## Performance Analysis

The runtime of this approach can be improved -- we are looping over the input data twice using a while loop and a for loop nested inside the while loop, so we are already looking at quadratic runtime. However, within the for loop we are also creating a set and checking if every course in the prereqs subset is present in ```sorted_schedule```, and at best this will be O(n) as we're checking every item in the course_reqs list. 

Final runtime is O(n^2) + O(n), which can be reduced to O(n^2).g