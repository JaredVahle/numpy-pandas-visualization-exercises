import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
#How many negative numbers are there?
len(a [a < 0])
#How many positive numbers are there?
len(a [a > 0])
#How many even positive numbers are there?
positive_a = (a [a > 0])
#If you were to add 3 to each data point, how many positive numbers would there be?
len(positive_a [positive_a % 2 == 0])
a_plus_three = a + 3
len(a_plus_three [a_plus_three > 0])
#If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2
a_squared.mean()
a_squared.std()
#A common statistical operation on a dataset is centering. 
#This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. 
#Center the data set.
a_squared
mean_of_a = a.mean()
centering_a = a - mean_of_a
centering_a
centering_a.mean()
standard_dev_of_a = a.std()
#Calculate the z-score for each data point. Recall that the z-score is given by:
z_score_a = centering_a/standard_dev_of_a
z_score_a


# Life w/o numpy to life with numpy


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
def sum_of_a(a):
    total = 0
    for num in a:
        total += num
    return total

sum_of_a = sum_of_a(a) 
sum_of_a

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

def mean(a):
    total = 0
    for num in a:
        total += num
    return total/ len(a)

mean_of_a = mean(a)
mean_of_a

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

def product(a):
    total = 1
    for num in a:
        total = total * num
    return total

product_of_a = product(a)
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

def square(a):
    squared_list = []
    for num in a:
        num = num ** 2
        squared_list.append(num)
    return squared_list
squares_of_a = square(a)
squares_of_a 

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

def odds(a):
    odd_list = []
    for num in a:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list
odds_in_a = odds(a)
odds_in_a
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

def evens(a):
    even_list = []
    for num in a:
        if num % 2 != 1:
            even_list.append(num)
    return even_list
evens_in_a = evens(a)
evens_in_a

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
np.max(b)
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
np.max(b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
np.mean(b)
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
np.mean(b)
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
np.square(b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odd_only = (b[b % 2 != 0])
odd_only
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

even_only = (b[b % 2 == 0])
even_only
# Exercise 9 - print out the shape of the array b.
np.shape(b)
# Exercise 10 - transpose the array b.
np.transpose(b)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b,1)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(b,(6,1))
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
np.min(c)
np.max(c)
np.sum(c)
np.product(c)

# Exercise 2 - Determine the standard deviation of c.

np.std(c)


# Exercise 3 - Determine the variance of c.

np.variance(c)
np.var(c)


# Exercise 4 - Print out the shape of the array c

np.shape(c)


# Exercise 5 - Transpose c and print out transposed result.

np.transpose(c)
c_transposed = np.transpose(c) 

# Exercise 6 - Get the dot product of the array c with c. 

np.dot(c,c)


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261


np.sum((c * c_transposed))

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

np.product((c * c_transposed))

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

np.sine(d)
np.sin(d)


# Exercise 2 - Find the cosine of all the numbers in d

np.cosine(d)


# Exercise 3 - Find the tangent of all the numbers in d

np.tangent(d)


# Exercise 4 - Find all the negative numbers in d

negative_d = (d[d < 0])


# Exercise 5 - Find all the positive numbers in d

positive_d = (d[d > 0])


# Exercise 6 - Return an array of only the unique numbers in d.

np.unique(d)


# Exercise 7 - Determine how many unique numbers there are in d.

len(np.unique(d))


# Exercise 8 - Print out the shape of d.

np.shape(d)


# Exercise 9 - Transpose and then print out the shape of d.

transposed_d = np.transpose(d)
np.shape(transposed_d)


# Exercise 10 - Reshape d into an array of 9 x 2

np.reshape(d(9,2))