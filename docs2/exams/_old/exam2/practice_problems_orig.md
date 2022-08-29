---
title: COSC 101&#58; Exam 2 Practice Problems
---


## Problem #1
Write a function that takes one parameter `n`, which is an integer, and prints a multiplication table of dimension `n`. This function should not return anything. You can assume that `n` will be greater than `0`. Use only `for` loops in your solution.

For example, if `n` is 3, your function should print:

```
1  2  3
2  4  6
3  6  9
```
[solution](practice_solutions#problem-1-solution)

&nbsp;

## Problem #2
Consider the following program:

```
inner = 0
outer = 0
other = 0
for ii in range(1,3):
    outer += 1
    other += ii
    for jj in range(1, -ii, -2):
        inner += 1
        other -= jj
print ('outer', outer)
print ('inner', inner)
print ('other', other)
```

(a) What is the output?

(b) The above code uses `for` loops. Translate the code to using just `while` loops.


[solution](practice_solutions#problem-2-solution)

&nbsp;

## Problem #3
Write a function that accepts a floating point (annualized) interest rate as a parameter, and returns the number of years it takes for an investment of $1 to double. The function should use a `while` loop.

[solution](practice_solutions#problem-3-solution)

&nbsp;

## Problem #4
Write a function named `countOdd` that takes a list of positive integers and returns the count of the odd values in the list.

[solution](practice_solutions#problem-4-solution)

&nbsp;

## Problem #5
Write a function that takes a list of integers `integer_list` as a parameter, and creates and returns a list with the even values from `integer_list`, each divided by 2. You should not modify the list passed as a parameter.

For example if the list `[1,3,4,8,7,5]` is passed as a parameter, the function should return the list `[2,4]` since the even values in the original list are `4` and `8`.

[solution](practice_solutions#problem-5-solution)

&nbsp;

## Problem #6
Write a function `sumSquares` that takes a list of numbers and computes and returns the sum of each number squared. For example, if the function is given the list `[2,3,4]` as a parameter, it should return `29 (4 + 9 + 16)`. The function should not modify the list passed as a parameter.

[solution](practice_solutions#problem-6-solution)

&nbsp;

## Problem #7
Write a function `is_subset` that takes two lists as a parameter and returns `True` if all the elements in the second list are also present in the first list (i.e., the second list forms a subset of the elements in the first list). Return `False` otherwise. 

[solution](practice_solutions#problem-7-solution)

&nbsp;

## Problem #8
Write a function that asks for a series of numbers until a "flag" value is entered (`-999`) and returns the floating point average of the numbers entered. If no numbers are entered, return the special value `None`.

[solution](practice_solutions#problem-8-solution)

&nbsp;

## Problem #9
Write a function that takes a list of integers representing daily low temperatures, in Fahrenheit degrees. Find the longest consecutive series of freezing temps (<= 32 degrees) in number of days, and return the average temperature of that series of temps. For example, given the list `[10,15,33,34,37,32,28,24,40]`, the function should return the average temp of the longest freezing streak `(32,28,24)`, which is `28`. You can assume that the list passed as a parameter is non-empty. If there are no freezing (or below) temperatures in the list, you should just return `None`. If there are streaks of the same length in the list, you can return the average of any of them.

[solution](practice_solutions#problem-9-solution)

&nbsp;

## Problem #10
Write a function that takes a list of strings and a one character string. Find and return the count of that character among all the strings in the list. For example, given the list `["apple","banana","pear"]`, and the character `"p"`, the function should return `3` (two p's in apple and one in pear).

[solution](practice_solutions#problem-10-solution)

&nbsp;

## Problem #11
Write a function that takes a list of integers as a parameters. Inside the function, do the following:

  1. Make one pass through each of the numbers in the list of integers.
  1. When ever you find a consecutive pair of numbers in which the second one is smaller than the first one, swap them.

For example, if you have the list `[3,2,1]`, you would:

  1. Swap `3` and `2`, giving `[2,3,1]`
  1. Swap `3` and `1`, giving `[2,1,3]`

This is the first step in implementing an algorithm called "bubble sort". If you notice what happened above, the largest element (`3`) "sunk" to the right, and the smaller elements are starting to "bubble up" to the left.

This function should not return anything, just modify the list "in place".

[solution](practice_solutions#problem-11-solution)

&nbsp;

## Problem #12
Write a function that takes a list of strings and an integer `N` and returns a new list in which all strings from the parameter list that are shorter than `N`. The function should not modify the list passed as a parameter.

[solution](practice_solutions#problem-12-solution)

&nbsp;

## Problem #13
Write a function that takes a string and returns `True` if all characters in the string are unique, and `False` otherwise.

[solution](practice_solutions#problem-13-solution)

&nbsp;

## Problem #14
Write a function that takes a list of integers, and returns a new list containing all the unique integers in the input (parameter) list (i.e., without any of the duplicate numbers).

[solution](practice_solutions#problem-14-solution)

&nbsp;

## Problem #15
In URLs on the web, spaces must get translated to a special sequence of characters (`'%20'`) in order to conform to what web browsers expect. Thus, the URL string `"http://example.com/a url with a space"` would need to get translated to `"http://example.com/a%20url%20with%20a%20space"`. Write a function that takes a string and returns a new string with any spaces replaced with `'%20'`. You cannot use any string methods or string slicing in your solution.

[solution](practice_solutions#problem-15-solution)

&nbsp;

## Problem #16
Consider the following two functions (assume the arguments are strings):

```
def cmpOne(s1,s2):
    if len(s1) > len(s2):
        print (s1)
    else:
        print (s2)

def cmpTwo(s1,s2):
    if len(s1) > len(s2):
        return s1
    else:
        return s2
```

Describe (in one to three sentences) how these functions differ. Include an example of something you can do with one that you can't do with the other.

[solution](practice_solutions#problem-16-solution)

&nbsp;

## Problem #17
Write a function that accepts a string (you may assume that this is a non-empty string containing only lower-case letters) and returns `True` if the first character comes before the last character (in alphabetical order) and returns `False` otherwise (e.g., if they are the same character or if the first character comes after the last character).

[solution](practice_solutions#problem-17-solution)

&nbsp;

## Problem #18
(a) Write a function that accepts one argument (you may assume that this is a non-empty string containing only lower-case letters) and returns the number of letters in the string that are strictly before `'h'` in the alphabet. For example, if your function is named `numBefore`, `numBefore('hello')` should return 1 (only `'e'` comes before `h`), and `numBefore('goodbye')` should return 4 (`g`, `d`, `b`, and `e` come before `h`). 

(b) The code for the problem above contains a definite loop therefore `for` loops solve the problem. For a little practice with `while` loops change the code to use just `while` loops.

[solution](practice_solutions#problem-18-solution)
