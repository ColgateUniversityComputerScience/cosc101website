---
title: COSC 101&#58; Exam 2 More Practice Problems
---


## Problem #1
Given a string `s` with an odd length:

  1. Write an expression to print the middle character. For example, if `s` is `'exam2'` the expression should print `'a'`.

  2. Write an expression to print the string up to but not including the middle character. For example, if `s` is `'exam2'` the expression should print `'ex'`.

  3. Write an expression to print from the middle character to the end, not including the middle character (i.e., from one after the middle to the end). For example, if `s` is `'exam2'` the expression should print `'m2'`.

[solution](more_practice_solutions#problem-1-solution)

&nbsp;


## Problem #2
Given the string `s='abcdefghij'`, write a string slice expression that will print the following:

  1. `'jihgfedcba'`

  2. `'adgj'`

  3. `'igeca'`

[solution](more_practice_solutions#problem-2-solution)

&nbsp;


## Problem #3
Write a function named `countsubstr` that takes two strings as parameters and returns the number of times that the second string appears in the first string. For example:

```python
>>> countsubstr('aabbabab','ab')
3
>>> countsubstr('computersarecomputational','comp')
2
```

You cannot use any built-in string methods for this problem (but you can use slicing).

[solution](more_practice_solutions#problem-3-solution)

&nbsp;


## Problem #4
Write a function `makeAcronym` that takes a phrase (a string) as a parameter, and creates and returns a new string that contains the first letter of each word in the phrase, capitalized. For example, `makeAcronym('Gnus not UNIX')` should return the string `'GNU'`. For this problem, you can use any string methods you'd like. For example: `upper()`, `lower()`, `count()`, `find()`, or `split()`.

[solution](more_practice_solutions#problem-4-solution)

&nbsp;


## Problem #5
Write a function `removeAs` that takes a string as input and returns the string with all `a`s removed. For example, if you call `removeAs('amalgamate')`, the function should return the string `'mlgmte'`. Your function should remove both lower-case and upper-case `A`'s but should not change any other characters.

[solution](more_practice_solutions#problem-5-solution)

&nbsp;


## Problem #6
Write a function `arrange_names` that takes a name in the form of `"Doyle, Arthur Conan"`, and returns the name in the form `"Arthur Conan Doyle"` (alphabetical order).

[solution](more_practice_solutions#problem-6-solution)

&nbsp;


## Problem #7
Write a function `guess_letters` that takes a word (a string) as a parameter and repeatedly asks the user to guess the letters in the word. The user should be asked for a new letter while he/she has not guessed all the letters in the word. Prior to each guess the user makes the function should print the letters that have been successfully guessed, as well as the number of letters remaining to be guessed. The function should return the number of guesses taken to get all the letters.

The guessing should all be done in a case-insensitive way (you can just convert to upper case everywhere). You are encouraged (but not required) to write a helper function.

[solution](more_practice_solutions#problem-7-solution)

&nbsp;


## Problem #8
Write a function `is_anagram` that takes two strings as parameters and to decide whether one is a permutation of the other. For example, if you are given `"cinema"` and `"iceman"`, you should return `True`, since these strings are anagrams.

[solution](more_practice_solutions#problem-8-solution)

&nbsp;


## Problem #9
Write a function `is_rotation` that takes two strings as parameters and tests whether one string is a rotation of another, e.g., `"waterbottle"` and `"erbottlewat"`. The function should return `True` if one string is a rotation of another and `False` otherwise.

[solution](more_practice_solutions#problem-9-solution)

&nbsp;


## Problem #10
Write a function called `maxStock` that takes a file name as a parameter (a string). Your function should find and return the stock symbol that has the highest value. The file will be structured as follows:

```text
AAPL 402.19
IBM 26.96
ORCL 31.11
IBM 186.12
```

Each line has two items: a stock symbol and a price, each separated by one or more spaces. For the example file above, your function should return `'AAPL'`, since it has the highest stock price.

[solution](more_practice_solutions#problem-10-solution)

&nbsp;


## Problem #11
Write a function `findeees` that reads a text file and returns a list of all words in the file that contain at least 3 `e`'s. The function should take one parameter, the name of the file to read. For this function, you can't use any built-in string methods. You can only use the len function on string objects, as well as basic string indexing.

[solution](more_practice_solutions#problem-11-solution)

&nbsp;


## Problem #12
Say that you have a text file in which the file only contains words (you can assume that the only characters in the file are letters and spaces).

Write a function called `wordCount` that takes two parameters: the file name (as a string) and a word to search for in the file. The function should return the number of occurrences of the word in the file. The letters in the file can be in both upper and lower case; your count should be done in a case-insensitive way (include any occurrence of the word regardless of case).

For example, if our file is named `'test.txt'` and has the contents (3 lines):

```text
cheese pickleS mayo mustard
pIcKlEs eggS tofu salt PEPPer
soy sauce mirin peanut BuTTer AND PiCKLES
```

`wordCount('test.txt', 'pickles')` should return `3`.

[solution](more_practice_solutions#problem-12-solution)

&nbsp;


## Problem #13
Write a function `averageLineLength` that computes and returns the average length of a line in a text file. The file name should be given as a parameter to the function. The function should just return the average line length (number of characters) as a floating point number.

[solution](more_practice_solutions#problem-13-solution)

&nbsp;


## Problem #14
Assume you have an input file `'data.txt'` that contains, on each line, a stock trading symbol, the daily low price per share, and the daily high price per share, each separated by spaces. You can assume that each symbol will be unique. For example, the file might have the following contents:

```text
AAPL 255 266
MSFT 22 24.1
GOOG 450 470.5
T 27.01 27.78
```

Write a program that finds the largest difference between the low and high share prices. The program should print the stock symbol as well as the difference between the low and high prices. For example, in the example data above, your program should identify print `GOOG had the biggest difference: 20.5`.

[solution](more_practice_solutions#problem-14-solution)

&nbsp;


## Problem #15
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

[solution](more_practice_solutions#problem-15-solution)

&nbsp;


## Problem #16
Write a function `countevens` that takes a list of integers as a parameter and returns a count of the number of even values in the list. For example:

```python
>>> countevens([2,1,2,3,4])
3
>>> countevens([2,2,1])
2
```

[solution](more_practice_solutions#problem-16-solution)

&nbsp;


## Problem #17
Write a function named `sum67` that takes a list of integers as a parameter, and returns the sum of the numbers, except that it should ignore sections of numbers that start with a `6`, extending to the next `7`. (You can assume that every `6` will be followed by at least one `7`). For example:

```python
>>> sum67([1,2,2])
5
>>> sum67([1,2,2,6,99,99,7,1])
6
>>> sum67([6,6,1,2,3,4,5,6,7,7])
7
```

[solution](more_practice_solutions#problem-17-solution)

&nbsp;


## Problem #18
Write a function `sumSquares` that takes a list of numbers and computes and returns the sum of each number squared. For example, if the function is given the list `[2,3,4]` as a parameter, it should return `29` (4 + 9 + 16).

[solution](more_practice_solutions#problem-18-solution)

&nbsp;


## Problem #19
Write a function `removeOdd1` that takes a list of integers as a parameter, and returns a new list that contains only the even (non-odd) numbers from the list passed as a parameter. You should not modify the list passed in as a parameter.

[solution](more_practice_solutions#problem-19-solution)

&nbsp;


## Problem #20
Write a function `removeOdd2` that takes a list of integers as a parameter and removes all the odd values in the list *in place*. The function should not return anything.

[solution](more_practice_solutions#problem-20-solution)

&nbsp;


## Problem #21
Write a function `mostFrequent` that finds the most commonly occurring items in a list, and returns a list of those items. For example given a list `[1,2,3,4,4,4,2,1,2,0,5]`, the function should return `[4,2]` since those items occur 3 times, which the maximum number of times any item occurs in the list. You can use any list methods.

[solution](more_practice_solutions#problem-21-solution)

&nbsp;


## Problem #22
Write a function `sumOddsLt7` that takes a list of positive integers and returns the sum of the odd values that are less than `7`. For example, if the list `[1,2,3,4,9,1,2,3,4]` is passed as the parameter, the function should return `8` (1+3+1+3).

[solution](more_practice_solutions#problem-22-solution)

&nbsp;


## Problem #23
Write a function `removeOddsLe7` that takes a list of positive integers and returns a new list of integers in which only even numbers less than or equal to `7` remain. The list passed as a parameter shouldn't be modified inside the function. For example, if the list `[1,2,3,4,9,1,2,3,4,9]` is passed as the parameter, the function should return the list `[2,4,2,4]`.

[solution](more_practice_solutions#problem-23-solution)

&nbsp;


## Problem #24
Write a function `secondLargest` that takes a list of integers as a parameter, and finds the second largest unique element in the list. To help, there are two useful functions built in to Python, `max` and `min`, that return the largest and smallest elements of a list, respectively.

You should not modify any element in the list. (You can make a copy of the list and modify the copy.)

```python
>>> secondLargest([1,2,3,3,4,4,5,5])
4
```

[solution](more_practice_solutions#problem-24-solution)

&nbsp;


## Problem #25
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

[solution](more_practice_solutions#problem-25-solution)

&nbsp;


## Problem #26
What is the output of the following code:

```python
def mystery1(xlist):
    while len(xlist) > 3:
        xlist.remove(max(xlist))

mylist = [ 42, 5, 10, 6, 7, 10, 4 ]
mystery1(mylist)
print (mylist)
```

[solution](more_practice_solutions#problem-26-solution)

&nbsp;


## Problem #27
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

[solution](more_practice_solutions#problem-27-solution)

&nbsp;


## Problem #28
Write a short program that, for each integer `k` between `2` and `N` (inclusive),  prints the number of positive integers up to and including `k` that evenly  divide into that number.  You should ask for the number `N` from the user. 

For example, your program's output might look like this (except for printing the actual divisors, which you don't need to do):

```
What is N? 6
2 has 2 divisors (1,2)
3 has 2 divisors (1,3)
4 has 3 divisors (1,2,4)
5 has 2 divisors (1,5)
6 has 4 divisors (1,2,3,6)
```

[solution](more_practice_solutions#problem-28-solution)
