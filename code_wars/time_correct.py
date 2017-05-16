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
'09:10:01'

>>> time_correct("11:70:10")
'12:10:10'

>>> time_correct("19:99:99")
'20:40:39'

>>> time_correct("24:01:01")
'00:01:01'

"""

def time_correct(t):
    if t == " ":
        return " "
    
    if t == None:
        return None

    if ":" in t:
    	h, m, s = map(int,t.strip().split(":"))

    else:
    	return 

    if s >= 60:
    	s = s%60
    	m = m + 1
    elif s < 10:
    	s = "0" + str(s)

    if m >= 60:
        m = m%60
        h = h + 1
    if m < 10:
    	m = "0" + str(m)
    if m == 0:
        m = "00"

    if h > 24:
        h = h%24
    if h < 10:
        h = "0" + str(h)
    elif h == 24:
        h = "00"

    time = str(h) + ":" + str(m) + ":" + str(s) 

    return time



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. !\n"