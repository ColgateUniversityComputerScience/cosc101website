# COSC 101 Homework 5: Fall 2022

The due date for this homework is **Thursday, October 13, 5:00pm**.

This homework will improve your skills with functions, docstrings and the doctest module. Specifically, this assignment is designed to give you practice with the following topics:

- Designing a program for a problem of your choosing in a modular fashion - by splitting it in its individual components (utility functions) and recombining them to solve the problem (in a main function).
- Using `docstring` to include documentation inside your functions.
- Using the `doctest` module to write unit tests for your functions.

As usual, we encourage you to start early.


# "Design Your Own Homework"

For this homework, you will select a problem/ task and use the Python skills you've acquired so far to **design a program** that solves this problem/ task. You are free to be creative and define your own problem/ task that you want to solve, or alternatively select one from a set of examples we offer. 

There are only a few requirements:

1) For this assignment **you are only required to write the program design**, that is the function signatures. **You are not expected to write the code that performs the actual computation inside the functions.** Just include the single statement `pass` for the body of each function.

2) You cannot select any problem/ task for which we have already written functions in class or lab sessions.  

3) Your program *must* be divided up into functions, including **a main function and at least two helper functions**. The requires for these functions are described below. 

4) **Optional/ Challenge step** For at least one of your helper functions, use comments to describe the *algorithm* you would use were you to actually write that function. The easiest way to describe the algorithm would be to list out the computations that are involved in the function.  


# Requirements for the functions

As a reminder, **you are not expected to write the code that performs the actual computation inside the functions.** Just include the single statement `pass` for the body of each function.


### Helper functions

Every helper function must take at least one parameter and return at least one value.

For each helper function, you must include:

1. The function definition
2. A docstring containing
    1. A description of the function.
    2. A list of input parameter names, types, and descriptions. 
    3. A description of the return value(s).
    4. At least three doctests, which cover both common and edge cases

### Main function

For the main function, you must include:

1. The function definition
2. A docstring containing a description of the function.
3. A sequence of comments in the function body (using #) that indicate how the different helper functions will come together. 

### Using `docstring` and the `doctest` module

A `docstring` is a string literal that occurs as the first statement in a function. You can find more information in the Python documentation on docstring: [https://www.python.org/dev/peps/pep-0257/](https://www.python.org/dev/peps/pep-0257/)

The `doctest` module allows you to write tests for individual functions within
the docstring of a function.  **All of the functions in your program must have at least three doctests** in them. You can find more information in the Python documentation on doctest:
[https://docs.python.org/3/library/doctest.html](https://docs.python.org/3/library/doctest.html).

### Examples of functions
Here's an example of two helper functions and a main function which uses the two helper functions for a very simple task/ problem. 

```
def isprime(n):
    '''
    Check if n is prime; return True if so, False otherwise.

    Parameters:
        n (int) - a decimal integer
    Returns:
        True/False (bool) - a boolean value indicating if n is prime or not

    >>> isprime(2)
    True
    >>> isprime(7)
    True
    >>> isprime(10)
    False
    '''
    pass
```

```
def multiples(x, n):
	'''
	Returns the first n multiples of some integer x. 

	Parameters:
		x (int) - the integer for which we want to compute the multiples of.

		n (int) - the number of multiples we want. 

	Returns:
		A string with the first n multiples of x separated by a space and comma. 

	>>> multiples(2, 5)
	'2, 4, 6, 8, 10'

	>>> multiples(50,0)
	''

	>>> multiples(-10,1)
	'-10'

	'''

	pass

``` 

```
def main():
	'''
	Prints the first 5 multiples of all prime numbers between 1 and 1000 in the following format: 

	2: 2, 4, 6, 8, 10
	3: 3, 6, 9, 12, 15

	and so on. 

	'''

	# Iterate through all numbers between 1 and 1000 using a for loop. 

	# For each number, check if it is prime by calling isprime(number).  

	# If the number is prime, get a string of all the multiples by calling multiples(number, 5).

	# Print the string.

	pass


```

# Example problems/ tasks you can choose from


## Prime Factorization Prompter 

Write a program that prompts the user to select one of the two options: factorization (f) or multiplication (m). If the user picks `f` for factorization, the program then prompts the user for a number and prints the prime factorization of that number. For example, the prime factorization for `360` is `2^3*3^2*5`. If the user picks `m` for multiplication, the program then prompts the user for the prime factorization of the number and prints the number corresponding to that prime factorization.

```
Select factorization (f) or multiplication (m): f
Enter a number to factorize: 360
The prime factorization of 360 is 2^3*3^2*5
```
```
Select factorization (f) or multiplication (m): m
Enter a prime factorization: 2^3*3^2*5
The number corresponding to the prime factorization 2^3*3^2*5 is 360
```


## Personal Webpage Template Generator

Write a program that produces the Hyper Text Markup Language (HTML) code for a personal webpage template. For a quick introduction to HTML please visit: [https://www.w3schools.com/html/html_intro.asp](https://www.w3schools.com/html/html_intro.asp).

The program first prompts the user for their name. The name will be used in the welcome message in the header of the webpage. The program then prints the HTML code for the webpage and terminates.


```
Type your name: Andrea Delgado-Olson

Copy this inside webpage.html file and open it in the browser:
<!DOCTYPE html>
<html>
<head>
<title>Personal Page</title>
</head>
<body>
<h1>Welcome to Andrea Delgado-Olson's Personal Page!</h1>
<img src="headshot.png" alt="headshot.png">
<h2>Info</h2>
<p>[Write your current position and contact information (phone, email and address)]</p>
<h2>Summary</h2>
<p>[Write a summary about yourself]</p>
<h2>Education</h2>
<p>[List your degrees in reversed chronological order]</p>
<h2>Experience</h2>
<p>[List your experience in reversed chronological order]</p>
<h2>Skills</h2>
<p>[List your most valuable skills]</p>
<h2>Certifications</h2>
<p>[List your certifications]</p>
<h2>Interests</h2>
<p>[List your interests]</p>
</body>
</html>
```

(_[Andrea Delgado-Olson](https://www.linkedin.com/in/andreadelgadoolson/) is the Founder of [Native American Women in Computing and STEM](https://www.linkedin.com/company/native-american-women-in-computing-and-stem/), the Executive Director of [Natives in Tech](https://nativesintech.org/), and previously was the Program Manager for [Systers](https://anitab.org/our-communities/systers/) and GHC Communities at [Anita B.org](https://anitab.org/)._)


## Haiku generator

A [haiku](https://en.wikipedia.org/wiki/Haiku) is a type of short form poetry that originated in Japan. A traditional haiku has three lines, each with 5, 7 and 5 syllables. 

Write a program that asks the user if they would like a Haiku. If the user says no, the program ends. If the user says yes, the program prints a haiku and asks the user if they would like another haiku and prints another one if the user says yes once again. This process goes on until the user says no. 

```
Welcome!

Would you like me to generate a Haiku? Yes

Warming christmastime
An aquatic, fast snail flaps
into the camel

Would you like another one? yes

Frigid wintertime
A tiny, hot kitten flaps
after the hamster

Would you like another one? No

Ok! You can just run the program again whenever you want more Haikus. 

```

The haikus in this example were generated from https://www.poem-generator.org.uk/haiku/


# Submission Instructions

You will submit two files for this assignment. 

1. A `hw5.py` file with your program design in it. Indicate in comments at the top of the program who worked on it and how long you spent.  Please remember to cite anyone from whom you received help, or any other sources of help (e.g., websites).

2. A `description.txt` which describes what the program is and why you chose to do what you did. 


# Grading

Your assignment will be graded on three criteria:

1. Program design [30%]: Program design should be *modular*, i.e. divided into several smaller functions to avoid code reuse and support unit testing.  Each helper function must take at least one parameter and return a value.

2. Docstrings [30%]: Each function must include a docstring. The docstrings for helper functions must also describe parameters and return values.

3. Doctests (at least three) for each helper function. [30%]
    
4. Code description [10%] including: (a) what the program is, and (b) why you chose to do what you did. 


