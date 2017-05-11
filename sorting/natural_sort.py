"""
This natural sort:

- sorts numbers before strings (instructions left this open)
- sorts strings case-insensitively ("apple" sorts the same as "Apple")
- sorts string with version numbers ("android1.2" < "android1.10")
- sorts dates ("2014-3-20" < "2014-12-21")
- sorts integers ("2" < "12")
- sorts negative integers -- IF at start of line ("-2" < "-1")

However:

I ran into ambiguity parsing dashes("-") and periods ("."). A dash in
a date is a separator, not a "this number is negative indicator".
A dot in a version number is a separator, not a real floating point
number ("android1.2" should come before "android1.10", whereas the
float 1.10 would come before 1.2).

I chose to handle dashes at the start of the line as a negative integer,
but anywhere else as a separator. I chose to not handle floating point
numbers at all, and treat all dots as separators.

The regex pattern captures negative numbers if the dash appears at the 
start of an item, but if the dashes appear in the middle of a string, 
(i.e. "YYYY-MM-DD") the dash will be treated as a string.  Decimal 
points are still considered strings, so that version numbers are 
evaluated correctly.  
"""


import re

def sort_strings(items):
    return print(sorted(items, key=natural_sort))

def natural_sort(item):
    # split on numbers (or negative numbers at start of item)
    sections = re.split('((?:^\s*-)?\d+)', item)  
    for i, section in enumerate(sections):
        if section[-1:].isdigit():    
            sections[i] = int(section)
        else:
            sections[i] = sections[i].lower()
    return sections

sort_strings(['1','3','2'])
sort_strings(['-2', '43', '-8', '24']) 
sort_strings(['Apple', 'Watermelon', 'bacon'])
sort_strings(['2016-10-12', '2016-10-10', '2017-01-01'])
sort_strings(['android2.2', 'Android13.0', 'iOS1.0', 'iOS1.3'])

# since I treat decimals as separators (to handle version #s properly),
# this sorts as -2.4, -1, 2, 10, .2 --- the dot at the start of .2
# gets treated as a string separator.

sort_strings(['-1','2','.2','10','-2.4'])

sort_strings(["a9", "ghi", "abc", "repeat", "2016/01/04", "2016/01/09", "a12", "2016-01-07", "a10", "Capitcalized", "123", "-2", "-20", "2016-01-02", "2017-02-03", "7.5", "-5.3", "a8.2", "abc123def", "repeat", "abc45def", "abc123efg"])