---
title: COSC 101&#58; Final Exam Practice Problems
math: true
---


## Expression Problems
Assume the following statements have already been executed in the interactive interpreter:

```python
>>> a = 'rain snow sleet'
>>> b = [a, 40, 21]
>>> c = { 21:'freezing', 40:'cold', 75:'warm', 97:'hot'}
```

For each of the following expressions, evaluate the expression and write the resulting value, or identify the error in the code that would prevent it from running.

### Expression 1
```python
>>> '7' in str(c[3])
```
[[solution](practice_solutions#expression-1-solution)]

### Expression 2
```python
>>> a[0::5]
```
[[solution](practice_solutions#expression-2-solution)]

### Expression 3
```python
print( 'temp is ' + str(sum(b[1:])/len(b[1:])) )
```
[[solution](practice_solutions#expression-3-solution)]

### Expression 4
```python
' or '.join([c[97], c[int('40')]])
```
[[solution](practice_solutions#expression-4-solution)]

### Expression 5
```
x = list(c.values())
x.sort()
print( x[0], a[:len(c)] )
```
[[solution](practice_solutions#expression-5-solution)]

### Expression 6
```
c['hamilton'] = { 'mon':31, 'tue':45, 'wed':40 }
print( c['hamilton']['tue'] )
```
[[solution](practice_solutions#expression-6-solution)]

&nbsp;

## More Expression Problems
Assume that the following statement have already been executed in the interactive interpreter:

```python
a = "radio cure"
b = [ 1, 1, 2, 3, 5 ]
c = { 'i':3, 'a': 7, 'e':5, 'o':2 }
```

For each of the following expressions, evaluate the expression and write the resulting value, or identify the error in the code that would prevent it from running.

  1. `(len(b) // 2) in c`

  2. `c[a.split()[2]] > len(a)`

  3. `a[2:-2:2]`

  4. `len(b) in c.values()`

  5. `len(b) in c.keys()`

  6. `b[::2].append(-13).sort()`

  7. `c[a[b.index(len(c)-1)]]`

  8. `c[a[1]] < c[a[-1]]`

[solution](practice_solutions#more-expression-problems)

&nbsp;






&nbsp;

<!--## Class Problems

### Class Problem 1
Define a class which has at least two methods:

  - `getString`: to get a string from console input
  - `printString`: to print the string in upper case.

Also include a simple test for each of the class methods. [[solution](practice_solutions#class-1-solution)]


### Class Problem 2
Write a definition for a class named `Kangaroo` with the following methods:

  - An `__init__` method that initializes an attribute named `pouch_contents` to an empty list.
  - A method named `put_in_pouch` that takes an object of any type and adds it to `pouch_contents`.
  - A `__str__` method that returns a string representation of the `Kangaroo` object and the contents of the pouch.

Test your code by creating two Kangaroo objects, assigning them to variables named `kanga` and `roo`, and then adding `roo` to the contents of `kanga`’s pouch.  [[solution](practice_solutions#class-2-solution)]


### Class Problem 3
Write a class called `Circle` that has a `radius` variable and related `get_radius` and `set_radius` methods. Write `get_area` and `get_circumference` methods that calculate and return the area and circumference based on the radius.

*Hint*: You can use the following formulas to calculate the area and circumferences of circles:

  - area = $$\pi r^2$$
  - circumference = $$2 \pi r$$

Write a `circle_areas()` function for your program that repeatedly asks the user to enter a radius for a circle until they enter done. For each circle entered, print the circumference. After the user is done entering new circles, your program should output the total area of all of the circles entered. [[solution](practice_solutions#class-3-solution)]


### Class Problem 4
Using the `Point` class from the textbook (shown below), write a program that asks the user for a number of points and determines their geometric center (or centroid).

```python
class Point:

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)
```

You program will have three functions: `main`, `get_points`, and `calculate_centroid`. Your `get_points` function should repeatedly ask the user for coordinates until they indicate they are finished and return a list of point objects. Your `calculate_centroid` function should take a list of point objects as a parameter and return a point object that is the centroid of the given points. Your `main` function should call each of the functions and print the results for the user.

*Hint*: The centroid point will have the coordinates $$(x_c, y_c)$$ where $$x_c$$ is the average of all $$x$$ coordinates of the points given and $$y_c$$ is the average of all $$y$$ coordinates of the points given.

[[solution](practice_solutions#class-4-solution)]
-->

&nbsp;

## Recursion Problems


### Recursion Problem 1
The Greatest Common Divisor (GCD) of two values can be computed using Euclid's algorithm.  Starting with the values $$a$$ and $$b$$, such that $$a > b$$, we repeatedly apply the formula: $$(a, b) = (b, a \bmod b)$$ until $$b = 0$$. At that point, $$a$$ is the GCD of the original $$a$$ and $$b$$.

In other words:
1. Starting with $$a > b$$
1. $$a =$$ (previous value of $$b$$)  
   $$b =$$ (previous value of $$a$$) $$\bmod$$  (the previous value of $$b$$)
1. Repeat previous step until $$b = 0$$
1. The final $$a$$ is the GCD of the original $$a$$ and original $$b$$

**(a)** Write a function that uses a *while* loop to implement Euclid's algorithm. The function should take two parameters: `a` and `b`. It should return the GCD of `a` and `b`. [[solution](practice_solutions#recursion-1a-solution)]

**(b)** Write a *recursive* function to implement Euclid's algorithm. Like the while-loop version, it should take two parameters `a` and `b`, and return the GCD between `a` and `b`. [[solution](practice_solutions#recursion-1b-solution)]


### Recursion Problem 2
Write a recursive function named `recursiveLetterCount(s, c)` that takes a string `s` and a character `c` as parameters (the second parameter is really a string, you can just assume it consists of only one character). The function should recursively count the number of occurrences of `c` in `s`.

Note: this isn't exactly what I'd consider a "naturally" recursive problem, but it is one that can be dealt with in a reduce-and-conquer manner, and thus can be solved recursively.

[[solution](practice_solutions#recursion-2-solution)]


### Recursion Problem 3
Write a recursive function that takes a list of integers as a parameter, and recursively computes and returns the sum of the list.  You can assume that there is at least one int in the list.

You'll have to think carefully about the base case and recursive case for this function. As one hint, the sum of a list with just one element, is the element itself. [[solution](practice_solutions#recursion-3-solution)]


### Recursion Problem 4
Write a recursive function `rpow(a,b)` that computes and returns $$a^b$$ (`a` raised to the `b`th power).

As a hint, consider that:

- $$a^b$$ is the same as $$a*a^{(b-1)}$$, and
- $$a^0$$ is equivalent to 1

You should not use the `**` operator anywhere in your solution. [[solution](practice_solutions#recursion-4-solution)]


### Recursion Problem 5
Write a recursive function to print out the digits of a number in English. For example, if the number is `153`, the output should be `"one five three"`. The function should take one integer as a parameter, and just print the number in English; it should not return anything.

As a hint, to get the rightmost digit of a (base 10) number, you can look at the remainder after dividing by 10 (`153 % 10` is `3`). To get the remaining digits, you can divide the number by 10 (`153/10` is `15`).

A restriction with this function is that you cannot convert the int to a string at any point: you must always work with the number as an int.

One more hint: for helping to print the words out, you can create a list of 10 strings, the element at index `0` is `'zero'`, element at index `1` is `'one'`, and so forth, like:

```python
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
```

[[solution](practice_solutions#recursion-5-solution)]


### Recursion Problem 6
Write a function called `removeNonLetters(s)` that takes one (possibly empty) string as a parameter, and returns a new string in which all the non-letters in the original string are removed. For example, `removeNonLetters('??? a b c !!!')` should return the string `'abc'`.

**(a)** Do this iteratively with a while loop. [[solution](practice_solutions#recursion-6a-solution)]

**(b)** Do this recursively. [[solution](practice_solutions#recursion-6b-solution)]


### Recursion Problem 7
Write a function that takes a string named `original` as a parameter, and produces a list of strings that contains all permutations of the characters in the `original` string. For example, if you're given the string `'abc'`, your function should return the list `['abc','acb','bac','bca','cab','cba']`. (The strings in the list can appear in any order.)

This problem is pretty hard, and recursion is the best way to solve it.

*Hint*: Think about how you can solve the problem for a string with one character, then a string with two characters. Keep building your solution so that you can handle a string of any length.

[[solution](practice_solutions#recursion-7-solution)]


&nbsp;

## Non-Recursive Problems 

### Other Problem 1
Write a function to compute the future value of an investment.  The function should take three parameters: the initial investment amount (the principal), the annual interest rate, and the number of years.  The function should return the value of the investment at the end of the number of years given.

Recall that the value of the investment after one year will be principal * (1 + annual_interest_rate).  You should not use the exponential formula for this problem.  Instead, you should use an accumulator pattern. [[solution](practice_solutions#other-1-solution)]


### Other Problem 2
Write a function to compute the square root of a sum of squares, also known as the "$$L^2$$ norm", over a list of numbers.

The function should be called `l2norm` and should take a list of numbers as a parameter.  Inside the function, you can compute the sum of each value in the list raised to the second power.  The function should then return the square root of this sum.  For example, the $$L^2$$ norm of `[2,3,4]` is the square root of ($$2^2$$ + $$3^2$$ + $$4^2$$).

Recall that you can compute the square root of a number using the `sqrt` function from the math module in Python.

Your function should work for a list of any size. [[solution](practice_solutions#other-2-solution)]


### Other Problem 3
What will the output of the following code be:
```python
def mystery1(xlist):
    while len(xlist) > 3:
        xlist.remove(max(xlist))

mylist = [ 42, 5, 10, 6, 7, 10, 4 ]
mystery1(mylist)
print( mylist )
```
[[solution](practice_solutions#other-3-solution)]


### Other Problem 4
What will the output of the following code be:
```python
def mystery2(n):
    if n == 0:
        return 0
    else:
        print( n )
        return n + mystery2(n-1)

t = mystery2(3)
print( t )
```
[[solution](practice_solutions#other-4-solution)]


### Other Problem 5
What will the output of the following code be:
```python
def mystery3(i, list1, list2):
    i = i + 4
    list1[-1] = 42
    list2 = list1

i = 2
one = [4, 10]
two = [-1, -1]
mystery3(i, one, two)
print( i )
print( one )
print( two )
```
[[solution](practice_solutions#other-5-solution)]


### Other Problem 6
Write a function `minTwo` that returns the smallest two unique elements in a list.  For example: `minTwo( [3, 4, 5, 3, 1, 9])` should return `1` and `3`.  You can either return a list of two elements or a tuple of two elements.  You can assume that there are at least two distinct elements in the list.

You can use any list method or function that you like, but you should not modify the list passed to the `minTwo` function in any way.
[[solution](practice_solutions#other-6-solution)]


### Other Problem 7
Use the following technique to write a function for estimating the value of $$\pi$$.

Suppose you have a round dart board that fits inside a square.  If you throw darts at random, the fraction that hit inside the circle versus those that hit outside the circle can be used to estimate $$\pi$$.  If `n` is the total number of darts randomly thrown (all of which can be assumed to land within the square), and `h` is the number that hit inside the circle, it can be shown that $$\pi$$ is approximately `4 * h/n`.

Write a function called `pidarts` that takes the number of darts as a parameter, and estimates $$\pi$$ by simulating that number of random dart throws.  You can use `2 * random.random() - 1` to generate the `x` and `y` coordinates of a random point within a 2x2 square centered at (0,0).  The dart hits inside the circle if its `x,y` coordinates satisfy the equation $$x^2 + y^2 <= 1$$.
[[solution](practice_solutions#other-7-solution)]


### Other Problem 8
Texting on mobile devices has spawned a set of abbreviations due to the need for writing and responding in compact and quick ways.  Create a dictionary of texting abbreviations and use it to write a teen-to-adult translator function.  The function should take one parameter, which is a string to translate (like "y r u l8?"), and return a new string, which is the translated expression ("why are you late?").  Your translation dictionary obviously cannot handle *all* translations, but it should handle at least 5.
[[solution](practice_solutions#other-8-solution)]


### Other Problem 9
Write a function that takes one string as a parameter.  Find and return a list of all the unique characters in the string.  Write two versions of this function:

**(a)** Only use lists. [[solution](practice_solutions#other-9a-solution)]

**(b)** Use a dictionary to keep track of unique letters (you still should return a list of unique letters at the end). [[solution](practice_solutions#other-9b-solution)]


### Other Problem 10
Consider expressing a fraction (numerator and denominator) as a tuple of two items, `(num, denom)`.  Write a function that takes two fractions as parameters and returns their sum.  The parameters will be in the form of `(numerator, denominator)` tuples, and the sum you return should also be in that form.

You don't need to reduce the final fraction, but you'll need to find a common denominator for the two fractions to add.  To do that, you can use $$(d_a*d_b)/gcd(d_a,d_b)$$, where $$d_a$$ and $$d_b$$ are the denominators for the two fractions, and `gcd(a,b)` is the Greatest Common Divisor (GCD) between the two numbers –see [recursion problem 1](practice_problems#recursion-problem-1). [[solution](practice_solutions#other-10-solution)]


### Other Problem 11
Given a list of `N` numbers, write a function to return a new list in which the numbers are shifted  circularly to the left by some integer `k` (where `k < N`).  The function should take a list and `k` as arguments, and return the shifted list.  The original list passed as a parameter should not be modified. [[solution](practice_solutions#other-11-solution)]


### Other Problem 12
Same problem as number 13, but with a tuple.  Write a function that takes a tuple of N numbers and a value k, and returns a new tuple in which the numbers are circularly shifted to the left k positions. [[solution](practice_solutions#other-12-solution)]


### Other Problem 13
Write a function that reads a text file containing a series of dictionary words, one per line, and finds all the pairs of words in which one word is equivalent to the other word spelled backwards.  The word pairs should be returned as a list of tuples (each tuple should contain a given word pair, all tuples of word pairs should be added to the list that is returned from the function). [[solution](practice_solutions#other-13-solution)]


### Other Problem 14
Write a function that takes a list of strings as a parameter and returns a new list in which the case (lower versus upper) of the characters of each string is swapped.  Example: if given the list `['aPpLe', 'AAPL', 'gOOglE', 'goog']`, your function should return the list `['ApPlE', 'aapl', 'GooGLe', 'GOOG']`.

**(a)** You cannot modify the list passed in as a parameter, but should create and return a new list.  Write a separate function to swap the case of one string, and it must be recursive.  You can use any methods you like. [[solution](practice_solutions#other-14a-solution)]

**(b)** You must modify the list passed as a parameter in place, and should not return anything. Your function to swap the case of one string should still be recursive. [[solution](practice_solutions#other-14b-solution)]


### Other Problem 15
Write a function that takes a file name (string) as a parameter, identifies numbers in the file, and returns a tuple containing the average and median of those numbers as a tuple.  

The file can be assumed to have the following structure:

  - The file consists of English text with words and numbers.  
  - Each word or number is separated by whitespace (spaces, tabs, newlines), and may end in a punctuation character.  
  - There are numbers intermixed with the words, which may also end in punctuation characters.

For example, here is an example of the kind of text that might appear in the file:

  ```text
  I once rode on a train with 55 elephants who ate 350 pounds of peanuts
  every 2 days.  47 clowns fed the elephants, but there were 2 slacker
  clowns that didn't do much.  The number of lion tamers on the train was 3,
  but there 0 lions on the train, which was odd.  
  ```

From the above text, you should find the numbers 55, 350, 2, 47, 2, 3, and 0  You can assume that all numbers in the file are integers.

Recall that the median is the number such that 50% of the values are larger than it, and 50% of the values are smaller than it.  If there are an odd number of values, there is a single median value.  If there are an even number of values, the median is the average of the two middle values.

Break this problem down into smaller tasks and use helper functions to keep each function SOFA. [[solution](practice_solutions#other-15-solution)]



### Other Problem 16
Write a spell checker function that takes the name of a text file as one parameter, and a list of valid dictionary words as the second parameter (note that this is a Python list, not a Python dictionary).  The valid dictionary words are each in lower case.  The function should return a list of words that do not appear in the dictionary of valid words.  You can assume that the list of valid words is in sorted order.  Try to make your function fast.

The text in the file can be assumed to be normal English text with punctuation, symbols, whitespace, etc.  Note that you'll need to "normalize" each word (strip out trailing punctuation characters, and put into lower case) before checking whether its in the list of valid words.  The list of invalid words you return should have each misspelled word in its original capitalization form, but without any punctuation. [[solution](practice_solutions#other-16-solution)]


### Other Problem 17
You have just created a competitor to Facebook.  Your app stores basic friendships in a Python dictionary such that the keys in the dictionary are user names, and the value for each key is a list of user names that are friends.  Here's an example of how the friendship information is stored (your site just started so there are only four users so far!):

```python
friendships = {
    'alice': ['bob'],
    'bob': ['alice','marvin','fred'],
    'fred':['bob','marvin'],
    'marvin':['bob','fred']
}
```

You can assume that all friendships are bidirectional (i.e., if a is a friend of b, then b is also a friend of a).

**(a)** Write a function that takes the friendship dictionary as a parameter, and returns the user that has the most friends.  For example, given the above dictionary, the function should return `'bob'`.  (For simplicity, you can assume that this function should just return 1 user with the most friends, even if there are ties for the most friends.) [[solution](practice_solutions#other-17a-solution)]

**(b)** Write a function that takes the friendship dictionary as a parameter and a user name, and returns a list of all the users that are "two friends away" from the user.  (That is, all the friends of your friends.)  The list should not contain any duplicates, and also not contain the name of the user passed as a parameter to the function.  For example, given the above dictionary and the user `'alice'`, the function should return friends of alice's friends, which are just: `['marvin','fred']`. [[solution](practice_solutions#other-17b-solution)]

## Other Problem #18
Write a function `is_subset` that takes two lists as a parameter and returns `True` if all the elements in the second list are also present in the first list (i.e., the second list forms a subset of the elements in the first list). Return `False` otherwise. Only use `while` loops in your solution. For example:

```python
>>> is_subset([1,2,3,4,5], [1,2,3])
True
>>> is_subset([1,2,3,4,5], [1,2,3,4,5,6])
False
>>> is_subset([1,2,3,4,5], [])
True
```

[solution](practice_solutions#other-problem-18-solution)

&nbsp;


## Other Problem #19
Write a function `average_of_freeze_streak` that takes a list of integers representing daily low temperatures, in Fahrenheit degrees. Find the longest consecutive series of freezing temps (<= 32 degrees) in number of days, and return the average temperature of that series of temps. For example:

```python
>>> print(average_of_freeze_streak([]))
None
>>> print(average_of_freeze_streak([33,40,50,60]))
None
>>> print(average_of_freeze_streak([30,40,45,37,33,30,29,28,40,45]))
29.0
```

Only use `while` loops in your solution. You can assume that the list passed as a parameter is non-empty. If there are no freezing (or below) temperatures in the list, you should just return `None`. If there are streaks of the same length in the list, you can return the average of any of them.

[solution](practice_solutions#other-problem-19-solution)

&nbsp;


## Other Problem #20
Write a function `count_chars` that takes a list of strings and a one character string. Find and return the count of that character among all the strings in the list. For example, given the list `["apple","banana","pear"]`, and the character `"p"`, the function should return `3` (two p’s in apple and one in pear).

You can only `while` loops in your solution. You must write a helper function.

[solution](practice_solutions#other-problem-20-solution)

&nbsp;


## Other Problem #21
Write a function `unique_chars` that takes a string and returns `True` if all characters in the string are unique, and `False` otherwise. You should use `while` loops in your solution (no `for` loops).

```python
>>> unique_chars('abcdefghijklmnopqrstuvwxyz')
True
>>> unique_chars('hello')
False
>>> unique_chars('help!')
True
```

[solution](practice_solutions#other-problem-21-solution)

&nbsp;


## Other Problem #22
Write a function `numBefore` that takes two parameters: a non-empty string and a single character string. The function returns the number of letters in the string that are strictly before the given character in the alphabet, ignoring case. For example:

```python
>>> numBefore('hello', 'h')
1
>>> numBefore('hello', 'z')
5
>>> numBefore('hello', 'a')
0
```

Your solution should only contain `while` loops; no `for` loops are allowed.

[solution](practice_solutions#other-problem-22-solution)

&nbsp;


<!-- The following problems used to be part of the Exam 3 review, but were moved here Spring 2020 when dictionaries were pushed to the final exam -->

## Other Problem #23
You have just created a competitor to Facebook. Your app stores basic friendships in a Python dictionary such that the keys in the dictionary are user names, and the value for each key is a list of user names that are friends. Here's an example of how the friendship information is stored (your site just started so there are only four users so far!):

```python
friendships = {
  'alice': ['bob'],
  'bob': ['alice','marvin','fred'],
  'fred':['bob','marvin'],
  'marvin':['bob','fred']
}
```

You can assume that all friendships are bidirectional (i.e., if `a` is a friend of `b`, then `b` is also a friend of `a`).

1. Write a function `most_friends` that takes the friendship dictionary as a parameter, and returns the user that has the most friends. For example, given the above dictionary, the function should return `'bob'`. (For simplicity, you can assume that this function should just return 1 user with the most friends, even if there are ties for the most friends.)

2. Write a function `friends_of_friends` that takes the friendship dictionary as a parameter and a user name, and returns a list of all the users that are "two friends away" from the user. (That is, all the friends of your friends.. The list should not contain any duplicates, and also not contain the name of the user passed as a parameter to the function. For example, given the above dictionary and the user `'alice'`, the function should return friends of alice's friends, which are just: `['marvin','fred']`.

[solution](practice_solutions#other-problem-23-solution)

&nbsp;


## Other Problem #24
Texting on mobile devices has spawned a set of abbreviations due to the need for writing and responding in compact and quick ways. Create a dictionary of texting abbreviations and use it to write a `teentoadult_translator` function. The function should take one parameter, which is a string to translate (like `"y r u l8?"`), and return a new string, which is the translated expression (`"why are you late?"`). Your translation dictionary obviously cannot handle *all* translations, but it should handle at least 5.

[solution](practice_solutions#other-problem-24-solution)

&nbsp;


## Other Problem #25
Write a function `uniqueletters_dict` that takes one string as a parameter. Find and return a sorted list of all the unique characters in the string. Do this only using a dictionary to keep track of unique letters (you still should return a list of unique letters at the end).

[solution](practice_solutions#other-problem-25-solution)

&nbsp;


## Other Problem #26
Write a function `remove_if_more_than_k` that takes two parameters: a list of integers and an integer `k`. The function should remove any values in the list that occur more than `k` times (removing all occurrences of that value). 

```python
>>> alist = [1,2,3,4,5,4,3,2,2,1,2]
>>> remove_if_more_than_k(alist, 2)
>>> print(alist)
[1,3,4,5,4,3,1,]
```

**Restrictions:** no list methods are allowed. To remove an item without using the remove method, you can say `del lst[x]` to remove an item at index `x`. You should *modify the list in place*, and the function should not return anything. All list items should remain in the same relative order when you're done. 

[solution](practice_solutions#other-problem-26-solution)
