# COSC 101 Homework 4: Fall 2022

The due date for this homework is **Thursday, October 6, 5:00pm EDT**.

This homework will improve your skills with functions, `for` loops (with `range`), and `if` statements by having you develop programs that use loops, conditionals, and accumulator patterns. Specifically, this assignment is designed to give you practice with the following topics:

- Conditional expressions and statements
- `for` loops over integers with `range`
- "accumulator patterns" with `for` loops
- functions

As usual, we encourage you to start early.

To get started, download [`hw4.zip`](hw4.zip) and unzip the compressed file to reveal the following files:

- `hw4_water.py`: this file will be used for [Part 1](#part-1-water-billing)

Note that all starter files have special headers at the top including form fields that you should fill out before submitting your assignment. Also, do not change the file names as the test program included with this homework (and test programs that we use) assume certain file names.

## Part 1: Water Billing

Clean water is an essential resource, and in most areas of the world it is not _free_.  In this part of the homework you will write a program to compute and display information for a utility company which supplies water to its customers.  The program will compute water usage and the bill for some number of customers, and compute and print the total billing amount for all customers.

Your program should prompt the user to enter three values (in the following order):

 1. The number of customers for which billing information should be prompted.

Then, for _each customer_, the program will ask:

 2. The customer's billing code (one character)
 3. The customer's beginning meter reading (a positive integer value) 
 4. The customer's ending meter reading (a positive integer value)

For each customer, the program will compute the number of gallons used, compute the bill amount, and print some summary information.  Once information for all customers has been gathered, the total amount billed to customers will be printed.

Below, some detail about the meaning and valid values for the above inputs is provided.

## Billing code

There are three valid billing codes: `r`, `c`, and `i`.  If an invalid code is input, the program should print an error statement and continue with getting information for the _next_ customer.

## Water meter readings

The meter is read by a representative of the utility company at the start and at the end of the billing period, and the readings are taken from a meter which has **nine digits** and records **tenths of a gallon**.  If an input is given that is not exactly 9 digits, an error message should be printed and the program should continue with getting information for the _next_ customer.

The meter's dial has nine digits and records tenths of a gallon. For example, assuming that the beginning reading was `444400003` and the ending reading was `444400135`, then the customer used `13.2` gallons of water during the billing period.

Since the meter's dial only has nine digits, the reading at the end of the billing period may be less than the reading at the beginning of the billing period. For example, assuming that the beginning reading was `999999997` and the ending reading was `000000005`, then the customer used `0.8` gallons of water during the billing period.

## Computing the bill

The bill amount depends on the billing code used, as follows:

Code 'r' (residential):
: $5.00 plus $0.0005 per gallon used

Code 'c' (commercial):
: $1000.00 for 4 million gallons or less, and $0.00025 for each additional gallon used

Code 'i' (industrial):
: $1000.00 if usage does not exceed 4 million gallons; $2000.00 if usage exceeds 4 million gallons but does not exceed 10 million gallons; and $2000.00 plus $0.00025 for each additional gallon if usage exceeds 10 million gallons.

Any prices printed should be rounded to the nearest cent (2 decimal places).  You should use the `round` function for that task.

## Program structure

In `hw4_water.py`, a set of _five_ functions to help you solve this problem has already been started.  In particular:

1.  The `valid_meter_reading` function should accept a **string** and return True or False, depending whether the string represents a valid 9-digit meter reading.  The function should return True if the reading consists of exactly 9 digit characters, and False otherwise.

2.  The `water_used` function should accept a beginning meter reading and an ending meter reading (which are both **valid** meter reading **strings**) and compute and return the water usage represented by the readings. The value returned should be a floating point number.

3.  The `compute_bill_amount` function should accept a billing code and an amount of water in gallons, and compute and return the bill amount.

4. The `one_customer` function should accept one parameter --- a customer number to use when creating input prompts.  The function should do the following:

 - It should first ask for a billing code for the customer.  If the billing code is invalid, the function should print an error message and return 0 .
 - It should then ask for the beginning meter reading for the customer and check if the reading is valid using the `valid_meter_reading` function.  If the reading is invalid, the function should print an error message and return 0.
 - The function should then ask for the ending meter reading for the customer, and do the same things as with getting the beginning meter reading.
 - The function should then compute the amount of water used using the `water_used` function.
 - After that, it should compute the bill amount using the `compute_bill_amount` function.
 - Finally, the function should print a summary for the customer, including the billing code, water usage in gallons rounded to the nearest tenth of a gallon, and print the bill amount.  It should then _return_ the bill amount.

5. Finally, the `main` function should prompt the user for the number of customers to input information for, then call the `one_customer` function exactly that many times.  It should compute and print the total billing amount (for all customers) based on results of calling `one_customer` for each customer.

## Example output

Here is an example of how your program's output should look.  Notice below that both customers have valid information:
```
How many customers? 2
Code for customer 1: r
Beginning meter reading for customer 1: 000001000
Ending meter reading for customer 1: 000002005
Customer 1: 
  Code: r
  Usage: 100.5
  Bill: $5.05
Code for customer 2: c
Beginning meter reading for customer 2: 100000000
Ending meter reading for customer 2: 200000000
Customer 2: 
  Code: c
  Usage: 10000000.0
  Bill: $2500.0
Total amount billed: $2505.05
```

Here is another example of how your program's output should look.  Notice below that all three customers have invalid information so the total amount billed is $0.

```
How many customers? 3
Code for customer 1: x
Invalid customer code
Code for customer 2: r
Beginning meter reading for customer 2: 10000000 # only 8 characters
Invalid begin reading
Code for customer 3: r
Beginning meter reading for customer 3: 100000000
Ending meter reading for customer 3: 99999kale # not all digits     
Invalid end reading
Total amount billed: $0
```

Credit: _This problem was inspired by a problem created by R. Enbody at Michigan State University._

# Testing

As with some other homeworks, we are providing a program that you can use to test that your homework is meeting the basic specifications of the assignment.

Please note:

  * The test program is **extremely** picky about spacing in the output (from print statements) your program produces.  If it reports an error, it might just be the difference of a single space.  

  * The test program is **NOT** a complete test.  You will still need to take responsibility for thoroughly testing your code before submitting.  However, our hope is that this test program will at least catch minor errors and make it easier for our grading process and more likely for you to receive full credit.

To use the test program, follow these steps:

1. Find the test program that is inside the zip file for this homework.  The file name is `hw4tester.py`.  Make sure that this file is in *exactly* the same folder as the homework files for this assignment.

2. Make sure your homework files are named exactly as described in assignment.

3. Open `hw4tester.py` in IDLE.  

4. In IDLE, select `Run` -> `Run module`

5. Read the test messages that are printed and revise your work accordingly.  If the output of your program does not precisely match the expected output, a test will fail.  An HTML file (a web page) will be created to show the exact differences between what your program prints and the expected output; if output does not match, you will see a message such as `View a detailed output comparison in hw4_water.py.html.` indicating the name of the file that you can open in your web browser.

We hope you find this helpful!

# Challenge problem

The challenge problem for this homework is to create a program that draws _scalable text art_.  
For example, [this fish](https://colgateuniversitycomputerscience.github.io/cosc101website/hw/hw04/fish.html) is 
generated by a program that asks for a _scale_ (some positive integer), then draws a fish of different scales/sizes depending on the integer input.

Note that the _scale_ captures some notion of the size of the art, but it is not necessarily equal to the width or height.  For example, in the fish, the scale is the number of rows in the tail of the fish (not including the row with just one `v`).

Note also that if you want to print a backslash character (`\`) you have to use a string of _two_ backslash characters `"\\"`.  Python uses the backslash character to produce special characters, like newline (`"\n"`), so you cannot just use a single backslash when printing that character out. For example:

    print("/\\/\\")

will print: `/\/\`

If you wish to do the challenge problem, create a file named `hw4_challenge.py`, and write your code for creating scalable text art in that file.  For inspiration, you can look at text art images here: https://www.asciiart.eu.  You can also do a search for "ASCII art" (ascii is the American Standard Code for Information Interchange; it defines a mapping between text characters and numeric equivalents --- in this context it simply means "plain text").

# Submission Instructions

 Please upload one Python file:

- `hw4_water.py`

If you've done the challenge problem, also upload `hw4_challenge.py`.

Remember to complete the questions at the top of the provided file and that the file you submit needs to have the exact filename.

# Grading

Your assignment will be graded on two criteria:

1. Correctness:  your program and the individual functions used to implement it must conform to the details described above.  Be sure to test your program for the various situations described above and that it works for other inputs, too.  [80%]

    The correctness part of your grade is broken down as follows:

    | Category | Portion of grade |
    | --- | --- |
    | `valid_meter_reading` function | 10% |
    | `water_used` function | 15% |
    | `compute_bill_amount` function | 20% |
    | `one_customer` function | 25% |
    | `main` function | 10% |

2.  Program design and style [20%]: style and program design become
    increasingly important the more complex your program becomes. For
    these programs, adhere to the following guidelines and the particular guidelines from your section:

    -   Variable names should be meaningful

    -   Programs should contain at least a few descriptive comments. Do
        *not* comment every line of code with low level explanations of
        what each line does. Focus on high level ideas.  

    -   All functions **must have docstrings** with a brief description of what the function does.
