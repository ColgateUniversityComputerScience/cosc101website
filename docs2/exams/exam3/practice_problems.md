---
title: COSC 101&#58; Exam 3 Practice Problems
---


## Problem #1
Assume that the following statement have already been executed in the interactive interpreter:

```python
a = "radio cure"
b = [ 1, 1, 2, 3, 5 ]
c = 3
```

For each of the following expressions, evaluate the expression and write the resulting value, or identify the error in the code that would prevent it from running.

  1. `len(b) // c`

  2. `b[5] > len(a)`

  3. `a[2:-2:2]`

  4. `c in b`

  5. `len(b[:3])`

  6. `b[::2].append(-13).sort()`

  7. `b.pop(2) == c`

  8. `a[-2] + a[5] + a[0]`

[solution](practice_solutions#problem-1-solution)

&nbsp;


## Problem #2
Given a string `s` with an odd length:

  1. Write an expression to print the middle character. For example, if `s` is `'exam3'` the expression should print `'a'`.
  
  2. Write an expression to print the string up to but not including the middle character. For example, if `s` is `'exam3'` the expression should print `'ex'`.
  
  3. Write an expression to print from the middle character to the end, not including the middle character (i.e., from one after the middle to the end). For example, if `s` is `'exam3'` the expression should print `'m3'`.

[solution](practice_solutions#problem-2-solution)

&nbsp;


## Problem #3
Given the string `s='abcdefghij'`, write a string slice expression that will print the following:

  1. `'jihgfedcba'`

  2. `'adgj'`

  3. `'igeca'`

[solution](practice_solutions#problem-3-solution)

&nbsp;


## Problem #4
Write a function named `countsubstr` that takes two strings as parameters and returns the number of times that the second string appears in the first string. For example:

```python
>>> countsubstr('aabbabab','ab')
3
>>> countsubstr('computersarecomputational','comp')
2
```

You cannot use any built-in string methods for this problem (but you can use slicing).

[solution](practice_solutions#problem-4-solution)

&nbsp;


## Problem #5
Write a function `makeAcronym` that takes a phrase (a string) as a parameter, and creates and returns a new string that contains the first letter of each word in the phrase, capitalized. For example, `makeAcronym('Gnus not UNIX')` should return the string `'GNU'`. For this problem, you can use any string methods you'd like. For example: `upper()`, `lower()`, `count()`, `find()`, or `split()`.

[solution](practice_solutions#problem-5-solution)

&nbsp;


## Problem #6
Write a function `removeAs` that takes a string as input and returns the string with all `a`s removed. For example, if you call `removeAs('amalgamate')`, the function should return the string `'mlgmte'`. Your function should remove both lower-case and upper-case `A`'s but should not change any other characters. 

[solution](practice_solutions#problem-6-solution)

&nbsp;


## Problem #7
Write a function `arrange_names` that takes a name in the form of `"Doyle, Arthur Conan"`, and returns the name in the form `"Arthur Conan Doyle,"` (alphabetical order).

[solution](practice_solutions#problem-7-solution)

&nbsp;


## Problem #8
Write a function `guess_letters` that takes a word (a string) as a parameter and repeatedly asks the user to guess the letters in the word. The user should be asked for a new letter while he/she has not guessed all the letters in the word. Prior to each guess the user makes the function should print the letters that have been successfully guessed, as well as the number of letters remaining to be guessed. The function should return the number of guesses taken to get all the letters. 

The guessing should all be done in a case-insensitive way (you can just convert to upper case everywhere). You are encouraged (but not required) to write a helper function. 

[solution](practice_solutions#problem-8-solution)

&nbsp;


## Problem #9
Write a function `is_anagram` that takes two strings as parameters and to decide whether one is a permutation of the other. For example, if you are given `"cinema"` and `"iceman"`, you should return `True`, since these strings are anagrams.

[solution](practice_solutions#problem-9-solution)

&nbsp;


## Problem #10
Write a function `is_rotation` that takes two strings as parameters and tests whether one string is a rotation of another, e.g., `"waterbottle"` and `"erbottlewat"`. The function should return `True` if one string is a rotation of another and `False` otherwise.

[solution](practice_solutions#problem-10-solution)

&nbsp;


## Problem #11
Write a function called `maxStock` that takes a file name as a parameter (a string). Your function should find and return the stock symbol that has the highest value. The file will be structured as follows:

```text
AAPL 402.19
IBM 26.96
ORCL 31.11
IBM 186.12
```

Each line has two items: a stock symbol and a price, each separated by one or more spaces. For the example file above, your function should return `'AAPL'`, since it has the highest stock price.

[solution](practice_solutions#problem-11-solution)

&nbsp;


## Problem #12
Write a function `findeees` that reads a text file and returns a list of all words in the file that contain at least 3 `e`'s. The function should take one parameter, the name of the file to read. For this function, you can't use any built-in string methods. You can only use the len function on string objects, as well as basic string indexing.

[solution](practice_solutions#problem-12-solution)

&nbsp;


## Problem #13
Say that you have a text file in which the file only contains words (you can assume that the only characters in the file are letters and spaces). 

Write a function called `wordCount` that takes two parameters: the file name (as a string) and a word to search for in the file. The function should return the number of occurrences of the word in the file. The letters in the file can be in both upper and lower case; your count should be done in a case-insensitive way (include any occurrence of the word regardless of case).

For example, if our file is named `'test.txt'` and has the contents (3 lines):

```text
cheese pickleS mayo mustard
pIcKlEs eggS tofu salt PEPPer
soy sauce mirin peanut BuTTer AND PiCKLES
```

`wordCount('test.txt', 'pickles')` should return `3`.

[solution](practice_solutions#problem-13-solution)

&nbsp;


## Problem #14
Write a function `averageLineLength` that computes and returns the average length of a line in a text file. The file name should be given as a parameter to the function. The function should just return the average line length (number of characters) as a floating point number.

[solution](practice_solutions#problem-14-solution)

&nbsp;


## Problem #15
Assume you have an input file `'data.txt'` that contains, on each line, a stock trading symbol, the daily low price per share, and the daily high price per share, each separated by spaces. You can assume that each symbol will be unique. For example, the file might have the following contents:

```text
AAPL 255 266
MSFT 22 24.1
GOOG 450 470.5
T 27.01 27.78
```
  
Write a program that finds the largest difference between the low and high share prices. The program should print the stock symbol as well as the difference between the low and high prices. For example, in the example data above, your program should identify print `GOOG had the biggest difference: 20.5`.

[solution](practice_solutions#problem-15-solution)

&nbsp;


## Problem #16
Write a function `median_of_file` that takes a file name (string) as a parameter. The file can be assumed to have the following structure: 

The file consists of English text with words and numbers. Each word or number is separated by whitespace (spaces, tabs, newlines), and may end in a punctuation character. There are numbers intermixed with the words, which may also end in punctuation characters.

For example, here is an example of the kind of text that might appear in the file:

```text
I once rode on a train with 55 elephants who ate 350 pounds
of peanuts every 2 days. 47 clowns fed the elephants, but 
there were 2 slacker clowns that didn't do much. The number 
of lion tamers on the train was 3, but there 0 lions on the 
train, which was odd. 
```

From the above text, you should find the numbers `55`, `350`, `2`, `47`, `2`, `3`, and `0`. You can assume that all numbers in the file are integers.

Your task is to recover all the integers from the text and return the median of the numbers. Recall that the median is the number such that 50% of the values are larger than it, and 50% of the values are smaller than it. If there are an odd number of values, there is a single median value. If there are an even number of values, the median is the average of the two middle values. The median of the numbers in the above file is `3`.

[solution](practice_solutions#problem-16-solution)

&nbsp;


## Problem #17
Write a function `countevens` that takes a list of integers as a parameter and returns a count of the number of even values in the list. For example:

```python
>>> countevens([2,1,2,3,4])
3
>>> countevens([2,2,1])
2
```

[solution](practice_solutions#problem-17-solution)

&nbsp;


## Problem #18
Write a function named `sum67` that takes a list of integers as a parameter, and returns the sum of the numbers, except that it should ignore sections of numbers that start with a `6`, extending to the next `7`. (You can assume that every `6` will be followed by at least one `7`). For example:

```python
>>> sum67([1,2,2])
5
>>> sum67([1,2,2,6,99,99,7,1])
6
>>> sum67([6,6,1,2,3,4,5,6,7,7])
7
```

[solution](practice_solutions#problem-18-solution)

&nbsp;


## Problem #19
Write a function `sumSquares` that takes a list of numbers and computes and returns the sum of each number squared. For example, if the function is given the list `[2,3,4]` as a parameter, it should return `29` (4 + 9 + 16).

[solution](practice_solutions#problem-19-solution)

&nbsp;


## Problem #20
Write a function `removeOdd1` that takes a list of integers as a parameter, and returns a new list that contains only the even (non-odd) numbers from the list passed as a parameter. You should not modify the list passed in as a parameter.

[solution](practice_solutions#problem-20-solution)

&nbsp;


## Problem #21
Write a function `removeOdd2` that takes a list of integers as a parameter and removes all the odd values in the list *in place*. The function should not return anything.

[solution](practice_solutions#problem-21-solution)

&nbsp;


## Problem #22
Write a function `mostFrequent` that finds the most commonly occurring items in a list, and returns a list of those items. For example given a list `[1,2,3,4,4,4,2,1,2,0,5]`, the function should return `[4,2]` since those items occur 3 times, which the maximum number of times any item occurs in the list. You can use any list methods.

[solution](practice_solutions#problem-22-solution)

&nbsp;


## Problem #23
Write a function `sumOddsLt7` that takes a list of positive integers and returns the sum of the odd values that are less than `7`. For example, if the list `[1,2,3,4,9,1,2,3,4]` is passed as the parameter, the function should return `8` (1+3+1+3).

[solution](practice_solutions#problem-23-solution)

&nbsp;


## Problem #24
Write a function `removeOddsLe7` that takes a list of positive integers and returns a new list of integers in which only even numbers less than or equal to `7` remain. The list passed as a parameter shouldn't be modified inside the function. For example, if the list `[1,2,3,4,9,1,2,3,4,9]` is passed as the parameter, the function should the list `[2,4,2,4]`.

[solution](practice_solutions#problem-24-solution)

&nbsp;


## Problem #25
Write a function `secondLargest` that takes a list of integers as a parameter, and finds the second largest unique element in the list. To help, there are two useful functions built in to Python, `max` and `min`, that return the largest and smallest elements of a list, respectively. 

You should not modify any element in the list. (You can make a copy of the list and modify the copy.)

```python
>>> secondLargest([1,2,3,3,4,4,5,5])
4
```

[solution](practice_solutions#problem-25-solution)

&nbsp;


## Problem #26
Write a function named `fractionsmaller` that takes a list of numbers and a single number as parameters. The function should return the fraction of values in the list that are smaller than the value given as the second parameter. You should not modify the list given as the first parameter.

For example:

```python
>>> fractionsmaller( [1,4,3,2,5], 3 )
0.4
>>> fractionsmaller( [5,2,3,6,10,2,55,3], 12 )
0.875
>>> fractionsmaller( [5,7,10], 4 )
0.0
>>> fractionsmaller( [1,2,3], 10 )
1.0
```

[solution](practice_solutions#problem-26-solution)

&nbsp;


## Problem #27
What is the output of the following code:

```python
def mystery1(xlist):
    while len(xlist) > 3:
        xlist.remove(max(xlist))

mylist = [ 42, 5, 10, 6, 7, 10, 4 ]
mystery1(mylist)
print (mylist)
```

[solution](practice_solutions#problem-27-solution)

&nbsp;


## Problem #28
What is the output of the following code:

```python
def mystery3(i, list1, list2):
    i = i + 4
    list1[-1] = 42
    list2 = list1

i = 2
one = [4, 10]
two = [-1, -1]
mystery3(i, one, two)
print(i)
print(one)
print(two)
```

[solution](practice_solutions#problem-28-solution)

&nbsp;

## Problem #29
Write a function `find_reverse_pairs` that reads a text file containing a series of words, one per line, and finds all the pairs of words in which one word is equivalent to the other word spelled backwards. The word pairs should be returned as a list of sublists (each sublist should contain a given word pair; all sublists of word pairs should be added to the list that is returned from the function).

For example, if the file contains:

```text
tic
tac
toe
computer
science
tab
bat
dog
cat
```

the resulting list will be `[['cat', 'tac'], ['bat', 'tab']]`.

[solution](practice_solutions#problem-29-solution)

&nbsp;

## Problem #30
Write a function `is_subset` that takes two lists as a parameter and returns `True` if all the elements in the second list are also present in the first list (i.e., the second list forms a subset of the elements in the first list). Return `False` otherwise. Only use `while` loops in your solution. For example:

```python
>>> is_subset([1,2,3,4,5], [1,2,3])
True
>>> is_subset([1,2,3,4,5], [1,2,3,4,5,6])
False
>>> is_subset([1,2,3,4,5], [])
True
```

[solution](practice_solutions#problem-30-solution)

&nbsp;

## Problem #31
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

[solution](practice_solutions#problem-31-solution)

&nbsp;


## Problem #32
Write a function `count_chars` that takes a list of strings and a one character string. Find and return the count of that character among all the strings in the list. For example, given the list `["apple","banana","pear"]`, and the character `"p"`, the function should return `3` (two p’s in apple and one in pear). 

You can only `while` loops in your solution. You must write a helper function. 

[solution](practice_solutions#problem-32-solution)

&nbsp;


## Problem #33
Write a function `unique_chars` that takes a string and returns `True` if all characters in the string are unique, and `False` otherwise. You should use `while` loops in your solution (no `for` loops).

```python
>>> unique_chars('abcdefghijklmnopqrstuvwxyz')
True
>>> unique_chars('hello')
False
>>> unique_chars('help!')
True
```

[solution](practice_solutions#problem-33-solution)

&nbsp;

## Problem #34
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

[solution](practice_solutions#problem-34-solution)

&nbsp;

<!-- more file i/o, exceptions, methods -->

## Problem #35

Consider a nested list that contains "shopping cart" items for an online store.  The nested list is structured as follows: each sublist contains (1) a product category, like "clothes", or "electronics", (2) a product name like "Merino wool socks, Unisex L, black", "1080p HD Adventure Camera", and (3) a product price as a floating point number.

Write a function called `cartCategorySum` that accepts two parameters: a nested list (as described above) and a category name.  The function should compute the sum of prices for all products within the given category.  Note that the category given as the second parameter to the function may be _in a different case_ than the category indicated in the list of cart items.

For example, `cartCategorySum([['toys', 'slinky', 1.5], ['toys', 'ball', 3.5], ['electronics', 'laser pointer', 11.99]], 'TOYs')` should return 5.0.


[solution](practice_solutions#problem-35-solution)

## Problem 36

Consider again a nested list that contains "shopping cart" items for an online store.  The nested list is structured as follows: each sublist contains (1) a product category, like "clothes", or "electronics", (2) a product name like "Merino wool socks, Unisex L, black", "1080p HD Adventure Camera", and (3) a product price as a floating point number.

Write a function called `cartCategoryProducts` that accepts two parameters: a nested list (as described above) and list of category names.  The function should return a list of products where the product category is contained in the category list.  The product name in the list returned should be given in "title case" (use the `title` method on strings).  The order of the items within the list returned doesn't matter.

For example, `cartCategoryProducts([['toys', 'slinky', 1.5], ['toys', 'ball', 3.5], ['electronics', 'laser pointer', 11.99]], ['TOYs'])` should return `['slinky', 'ball']`.

[solution](practice_solutions#problem-36-solution)

## Problem 37

Consider again a nested list that contains "shopping cart" items for an online store.  The nested list is structured as follows: each sublist contains (1) a product category, like "clothes", or "electronics", (2) a product name like "Merino wool socks, Unisex L, black", "1080p HD Adventure Camera", and (3) a product price as a floating point number.

Write a function called `sortCartProducts` that accepts one parameter: a nested list (as described above).  The function should create a new list containing sublists of _only_ the product name and price, with product names in "title case" (use the `.title()` string method).  The list contents should be sorted by product price in _descending_ numeric order (i.e., most expensive items first).  The `sortCartProducts` should *not* modify the list given as a parameter.

For example, `sortCartProducts([['toys', 'slinky', 1.5], ['toys', 'ball', 3.5], ['electronics', 'laser pointer', 11.99]])` should return `[['laser pointer', 11.99], ['ball', 3.5], ['slinky', 1.5]]`.

[solution](practice_solutions#problem-37-solution)

## Problem 38

Assume that a text file with product categories, product names, and product prices exists, and has the following structure: category names are listed on lines by themselves, followed by 0 or more lines with a product name and product price, separated by a semicolon.  For example:

```
toys
slinky; 1.5
ball; 3.5
electronics
laser pointer; 11.99
```

Write a function `loadInventory` that accepts a filename (a string) as a parameter, and creates and returns a nested list similar to above problems (e.g., problem 37).  If the file represented by the given filename does not exist, the function should _not_ crash and return an empty list.

[solution](practice_solutions#problem-38-solution)
