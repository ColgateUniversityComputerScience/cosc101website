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
Write a function that takes a string and character and replaces all instances
of that character with asterisks (`*`). You may not use the `replace`
string method.

[solution](practice_solutions#problem-4-solution)

&nbsp;

## Problem #5
Write a function that asks for a series of numbers until a "flag" value is entered (`-999`) and returns the floating point average of the numbers entered. If no numbers are entered, return the special value `None`.

[solution](practice_solutions#problem-5-solution)

&nbsp;

## Problem #6
Write a function that takes a string and returns `True` if all characters in the string are unique, and `False` otherwise.

[solution](practice_solutions#problem-6-solution)

&nbsp;

## Problem #7
In URLs on the web, spaces must get translated to a special sequence of characters (`'%20'`) in order to conform to what web browsers expect. Thus, the URL string `"http://example.com/a url with a space"` would need to get translated to `"http://example.com/a%20url%20with%20a%20space"`. Write a function that takes a string and returns a new string with any spaces replaced with `'%20'`. You cannot use any string methods or string slicing in your solution.

[solution](practice_solutions#problem-7-solution)

&nbsp;

## Problem #8
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

[solution](practice_solutions#problem-8-solution)

&nbsp;

## Problem #9
Write a function that accepts a string (you may assume that this is a non-empty string containing only lower-case letters) and returns `True` if the first character comes before the last character (in alphabetical order) and returns `False` otherwise (e.g., if they are the same character or if the first character comes after the last character).

[solution](practice_solutions#problem-9-solution)

&nbsp;

## Problem #10
(a) Write a function that accepts one argument (you may assume that this is a non-empty string containing only lower-case letters) and returns the number of letters in the string that are strictly before `'h'` in the alphabet. For example, if your function is named `numBefore`, `numBefore('hello')` should return 1 (only `'e'` comes before `h`), and `numBefore('goodbye')` should return 4 (`g`, `d`, `b`, and `e` come before `h`). 

(b) The code for the problem above contains a definite loop therefore `for` loops solve the problem. For a little practice with `while` loops change the code to use just `while` loops.

[solution](practice_solutions#problem-10-solution)
