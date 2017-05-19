
"""
PROBLEM 1:

There are 10 products and the average price is $100. The cheapest item is $20 and there are exactly

4 items lower than $40. What is the maximum price that any item can be? Please include your work and

list any assumption(s) that you make to arrive at your answer.


If there are 10 products and the average price is $100, we can assume that 10 * $100 gives us the total price of $1000 for all items.

If we want to find the maximum possible price for a single item, we need to set the 4 items under $40 to the cheapest possible price, which is $20. Subtracting ($20 * 4 = $80) from $1000 gives us $920.

Now we have 6 items left, which need to be priced at $40 or above. If we reserve 1 item to be our max price, we can set the remaining 5 items to $40 each. Subtracting (5 * $40 = $200) from $920 gives us $720 for our last item, and gives our maximum price for a single item.

4 * 20 =	 80
5 * 40 =	200
1 * 720 =	720
----------------   
		   1000	


PROBLEM 2: 

In a particular code, the digits from 0 to 9 inclusive are each represented by a different letter of the

alphabet, the letter always representing the same digit. In case the following sum

B O P B + S K B = C V B Q

holds true when it is expressed in digits, which of the following cannot be properly inferred:

(A) B cannot be 0.

(B) B must be less than 5.

(C) Q must be even.

(D) O + S must be greater than 8.

(E) C must be greater than B by 1


 B O P B
+  S K B
---------
 C V B Q

Order of Inference: 

1 => (A) can be true because if B = 0, then B + B = B. However, in the given code, B + B = Q.

5 => (B) This leaves B < 5 as the condition that can't be inferred, as we have no supporting evidence. 

2 => (C) can be true because if you add the same number twice, you must get an even number. 

4 => (D) This is actually reliant on E being true. Because we can infer that O + S results in a sum large enough to carry over to B + " " and resulting in C (instead of just B + " " = B), we can infer that 0 + S is greater than 8. 

3 => (E) can be true because B + " " = C. We can infer that (O + S) = V carried over to B, resulting in C. 


PROBLEM 3:

Divide $97 into a number of bags so that I can ask for any amount between $1 and $97, and you can

give me the proper amount by giving me a certain number of these bags without opening them. Use

whole $ increments. What is the minimum number of bags you will require?

This requires that we are able to represent numbers using smaller numbers that sum up to the original number. For example, starting with 1 and 2, we can represent 3 as 2 + 1 and so on: 4 (4), 5 (4 + 1), 6 (4 + 2), and 7 (4 + 2 + 1 ). To represent 8, we need to start a new bag like we did with 4 -- once we reach a number that is twice the previous bag, we need to instantiate that bag. This doubling/halving concept for representation is similar to how decimal numbers are represented in binary.

Therefore to represent $97, we need at least: 

$1, $2, $4, $8, $16, $32, $64, $128 => 8 bags 

"""


"""
PROBLEM 4: SQL

You have the following MySQL table named revenue. Each row represents a sale by a given person

(name). Construct a query that will output the name of the person that made the most gross revenue and

the associated gross revenue. Include the answer. Assume revenue is USD.

name product revenue

A z 100

B z 50

A x 35

C x 40

C z 70

B y 55

B x 65

sqlite> select * from revenue;

name|product|revenue
A|z|100
B|z|50
A|x|35
C|x|40
C|z|70
B|y|55
B|x|65

sqlite> SELECT name, sum(revenue) FROM revenue GROUP BY name;

name|sum(revenue)
A|135
B|170
C|110

(B, 170) had the highest gross revenue.

PROBLEM 5: SQL JOINS

You now have a table the describes the product. Using this table and the revenue table above,

construct a query to show who has the highest revenue of new products.

product status

x new

y discontinued

z new

sqlite> select * from product;

product|status
x|new
y|discontinued
z|new

sqlite> select name, sum(revenue) from revenue join product on revenue.product = product.product where status = 'new' GROUP BY name;
name|sum(revenue)

A|135
B|115
C|110

(A, 135) has the highest revenue of new products.

"""

"""
PROBLEM 6: Python

In 20 lines of code or fewer (not counting import lines), write Python code that when run as:

$ wordfrequencies.py URL 

prints the output like below, which is the n most frequent words (defined as non-space characters

separated by space characters) at URL (do not be case sensitive; The == the)

$ wordfrequencies.py http://www.infomat.net/infomat/library/aliceinwonderland.txt

the     |       1668

and     |       798

to      |       755

a       |       640

of      |       542

she     |       518

said    |       421

it      |       377

in      |       366

was     |       333

NOTE: See word_frequencies.py 
"""


"""
PROBLEM 7: XML

Write an XML document that contains the following:

- Encoding is ISO-8859- 1

- A Document Type Definition (DTD) that defines this is a document of type note

- note element has four elements: to, from, subject, body

- Declare that the child element to must occur one or more times inside the note element

- Declare that the elements to, from, and subject are of the type &quot;#PCDATA&quot;

- Declare that the element body is of the type &quot;#CDATA&quot;

- The element subject has an attribute called date with the value &quot;03/14/1592&quot;

Use the following as the data:

to -&gt; John

from -&gt; Jane

subject -&gt; Reminder

body -&gt; Don&#39;t forget that 35 &lt; 50!
"""


"""
PROBLEM 8: REGEX - Validate phone number
"""
# import re

# def valid_phone(num):
# 	"""
# Construct a regular expression that will validate a standard U.S. Phone number.

# >>> valid_phone('555-555-5555')
# 555-555-5555 is a valid US number.

# >>> valid_phone('0')
# Sorry! 0 is not a valid US number.

# >>> valid_phone('cat')
# Sorry! cat is not a valid US number.

# >>> valid_phone('555 555 5555')
# 555 555 5555 is a valid US number.

# >>> valid_phone('(555)555-5555')
# (555)555-5555 is a valid US number.

# >>> valid_phone('5555555555')
# 5555555555 is a valid US number.

# 	"""
# 	# resp = re.match('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$', num)
# 	resp = re.match('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', num)
# 	num_input = str(num)

# 	if resp:
# 		print("%s is a valid US number." %num_input)

# 	else:
# 		print("Sorry! %s is not a valid US number." %num_input)

# 	return


# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print "SUCCESS!"