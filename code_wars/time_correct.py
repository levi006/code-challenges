"""
A new task for you!

You have to create a method, that corrects a given time string. There was a problem in addition, so many of the time strings are broken. Time-Format is european. So from "00:00:00" to "23:59:59". 

Some examples:

"09:10:01" -> "09:10:01"
"11:70:10" -> "12:10:10"
"19:99:99" -> "20:40:39"
"24:01:01" -> "00:01:01"

If the input-string is null or empty return exactly this value! (empty string for C++)
If the time-string-format is invalid, return null. (empty string for C++)

>>> time_correct(" ")
' '

>>> time_correct("09:10:01")
"09:10:01"

>>> time_correct("11:70:10")
"12:10:10"

>>> time_correct("19:99:99")
"20:40:39"

>>> time_correct("24:01:01")
"00:01:01"

"""

def time_correct(t):
    if t == " ":
        return " "
    
    if t == None:
        return None


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"