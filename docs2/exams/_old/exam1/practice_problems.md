---
title: COSC 101&#58; Exam 1 Practice Problems
math: true
---


## Problem #1
Consider the following lines of code:

```
a = 3
b = 2
c = 5
```

What values result from the following expressions?

1. `a**b/2+1`<br /><br />
1. `c//a`<br /><br />
1. `5%a`<br /><br />
1. `a*float(b)/10`<br /><br />
1. `'a' * 3 + 'h!'`<br /><br />
1. `a/2.0 == 1.5`<br /><br />
1. `True and c == a`<br /><br />
1. `not True or c > b`<br /><br />

*Check your answers by typing this code into IDLE*

&nbsp;


## Problem #2
Consider the following lines of code:

```
a = 8
b = 1.1
c = 5
d = '9'
```

What values result from the following expressions?

1. `int(b) > (a // c)`<br /><br />
1. `d * (int(d) % c) + '!'`<br /><br />
1. `float(d) - c`<br /><br />
1. `c/a <= b`<br /><br />
1. `int(d*2) > a or int(b) > int(d)`<br /><br />

*Check your answers by typing this code into IDLE*

&nbsp;


## Problem #3
For each of the following expressions, evaluate the expression and write the resulting value, or identify the error in the code that would prevent it from running.

1. `3**2/2+1`<br /><br />
1. `5 = x`<br /><br />
1. `7%3 == 2`<br /><br />
1. `(3**234235 > 5) or (4 != (3+1))`<br /><br />
1. `"average score is " + (90.0 + 80.0)/2`<br /><br />

*Check your answers by typing this code into IDLE*

&nbsp;


## Problem #4
The U.S. census provides information on its web page about the current U.S. population as well as approximate rates of change. Three rates of change are provided:

- a birth every 7 seconds
- a death every 13 seconds
- a new immigrant every 35 seconds

These are obviously approximations, but they can assist in providing population estimates in the near term. Write a program asks the user for a number of years and displays the estimated population. You can assume that the current population is 307,357,870, and that there are 365 days in a year (i.e., ignore leap years).

[solution](practice_solutions#problem-4-solution)

&nbsp;


## Problem #5
Write a short program that prompts for an integer `N`, and then finds and prints sum of consecutive integers from `1` up to `N`.  That is, if `N` is `5`, your program should print `15` (`1+2+3+4+5`).

[solution](practice_solutions#problem-5-solution)

&nbsp;


## Problem #6
Expand the previous program so that it prints every sum `1..k` for `k` between `1` and `N`.  For example, if `N` is `5`, your program should print:

```
1
3
6
10
15
```

That is, it should print `1`, `1+2`, `1+2+3`, `1+2+3+4`, and `1+2+3+4+5`.


[solution](practice_solutions#problem-6-solution)

&nbsp;


## Problem #7
Write a program that asks the user for a number of knuts (the currency in the Harry Potter series), and convert the given number of knuts to sickles and galleons.  There are 29 knuts in one sickle, and 17 sickles in one galleon.  Perform the calculation and print only non-zero values.  That is, if there are not enough knuts for there to be one sickle, don't print "0 sickles"

[solution](practice_solutions#problem-7-solution)

&nbsp;


## Problem #8
Write a program to read an integer entered by the user.  If the number entered is an even number print "`even`"; if it is an odd number print "`odd`".  If it is evenly divisible by 4 and evenly divisible by 7, print "`divisible by 4 and 7`".  (Note that some numbers, such as 28, are both evenly divisible by 4 and 7, and are even; in such cases you should print out both "`even`" and "`divisible by 4 and 7`".)

[solution](practice_solutions#problem-8-solution)

&nbsp;


## Problem #9
Write a program to compute and print the average snowfall per day in a month, assuming there are 28 days in the month (i.e., it is February in a non-leap year).  In addition, your program should print the maximum daily snowfall amount.

The program should first ask for the number of days it snowed in the month.  You can assume that the number of days entered is between 0 and 28 (you do not need to check that the user entered a valid value). Next, the program should repeatedly ask for the amount of snowfall for each day that it snowed.  You can assume that the values entered are integers referring to the number of centimeters of snow.  Your program should then report the average snowfall per day in the month, which may include a fractional part, and print the maximum daily snowfall.

Here is an example run where the user entered the snowfall amount for four days:

```
How many days did it snow in February? 4
Enter snowfall amount: 4
Enter snowfall amount: 10
Enter snowfall amount: 20
Enter snowfall amount: 6
The average snowfall per day is 1.42857142857 cm.
The maximum daily snowfall is 20 cm.
```

Here is an example run where the user entered the snowfall amount for two  days:

```
How many days did it snow in February? 2
Enter snowfall amount: 16
Enter snowfall amount: 12
The average snowfall per day is 1.0 cm.
The maximum daily snowfall is 16 cm.
```

[solution](practice_solutions#problem-9-solution)

&nbsp;


## Problem #10
Consider the following program:

```
if myVar % 2 == 1:
    if myVar**3 != 27:
        myVar = myVar + 4    # assignment 1
    else:
        myVar = myVar / 1.5  # assignment 2
else:
    if myVar <= 10:
        myVar = myVar * 2    # assignment 3
    else:
        myVar = myVar - 2    # assignment 4
print (myVar)
```

Find four values of `myVar` that each cause one of the four assignment statements to be executed such that all four statements will be executed. 

[solution](practice_solutions#problem-10-solution)

&nbsp;


## Problem #11
A day has 86,400 seconds (24*60*60).  Given a number in the range 1 to 86,400, output the current time in hours, minutes, and seconds with a 24-hour clock.  

For example, 70,000 seconds is 19 hours, 26 minutes, and 40 seconds.

[solution](practice_solutions#problem-11-solution)

&nbsp;


## Problem #12
This problem involved concepts not yet covered in class and has been removed.

&nbsp;


## Problem #13
Write a program to print a table of interest earned on an investment, and the investment value, for some number of years.  Ask the user for (1) the amount to initially invest, (2) the interest rate, and (3) the number of years to invest.  Your program should print, for each year, the current investment value and the total amount of interest earned.  

For example, if the user enters $100 as the investment, 0.05 as the interest rate (5%), and 10 years, the program should print the following:

```
Year    Total investment value    Interest earned
----    ----------------------    ---------------
0       100.0                     0.0
1       105.0                     5.0
2       110.25                    10.25
3       115.76                    15.76
4       121.55                    21.55
5       127.63                    27.63
6       134.01                    34.01
7       140.71                    40.71
8       147.75                    47.75
9       155.13                    55.13
10      162.89                    62.89
```

You should not use the exponential formula for this problem; use an accumulator pattern.

[solution](practice_solutions#problem-13-solution)

&nbsp;


## Problem #14
Write a program to compute an approximation to pi (\\(\pi\\)) using the Wallis product.  Your program should ask the user for a number n and compute an approximation that is based on the following series:

\\( \frac{\pi}{2} \approx \frac{2}{1} * \frac{2}{3} * \frac{4}{3} * \frac{4}{5} * \frac{6}{5} * \frac{6}{7} * \frac{8}{7} * \frac{8}{9} * \frac{10}{9} * \ldots \\)

With 4 terms, the estimate for \\(\pi\\) is approximately 2.844; with 10 terms, it is approximately 3.002; with 10,000 terms, it is approximately 3.141.  

Hints: 

- Notice that this is a product, not a summation.
- Notice that the sequence above is an actually estimate for pi/2.  You will need to multiply by 2 to get an estimate for pi
- If you look at the terms in pairs, you can see a pattern.  In each pair, the numerator is the same and denominators are similar (the denominator of the second term is 2 larger than the first).  Write a for loop that loops n/2 times and each time through the loop, it incorporates the next pair of terms.  You can assume that n is always even.
- Alternatively, you might notice a pattern among the first, third, fifth, etc. terms and a slightly different pattern among the second, fourth, sixth, etc. terms.  You can write a for loop that uses an if statement to alternate between two patterns.


[solution](practice_solutions#problem-14-solution)

&nbsp;


## Problem #15
Write a program that prints all the multiples of 6 that are between 10 and 56, inclusive.  In other words, write a program that prints the following sequence of numbers:

```
12
18
24
30
36
42
48
54
```

[solution](practice_solutions#problem-15-solution)

&nbsp;


## Problem #16
Write a program that asks for one integer and computes and prints whether the integer is a prime number or not.   

Remember, a prime number is one that can't be evenly divided by any other number except 1 and itself.  For example, no (positive) integer divides evenly into 7 except 1 and 7.


[solution](practice_solutions#problem-16-solution)

&nbsp;


# Problem #17
Predict what the output will be for the following short programs **without running them on the computer**. If you expect there will be an error, state what type of error occurs,  where it occurs and why. Assume each question is run as a separate program (not in the interpreter). 


1. &nbsp;

        x = input("Enter some input: ")
        print(type(x))
      
   At the prompt the user entered: 42.3<br /><br />

1. &nbsp;

        m = 24
        n = input("Enter a word: ")
        print(type(n))
        print(str(n))
        print(m / int(n))
        
   At the prompt the user entered: '6'<br /><br />

1. &nbsp;

        p = input("Enter an integer: ")
        q = input("Enter any number: ")
        r = float(p)
        s = float(p)
        t = r + s ** 3 / 2 * r + s / 3
        print(t)
           
   At the first prompt the user entered: 5  
   At the second prompt the user entered: 2.9<br /><br />

1. &nbsp;

        a = input("Enter a number: ")
        b = int(a)
        c = b + b * b ** 2 / 8
        d = a + str(c)
        if (c < 100):
           print(d)
        else:
           print(c)
        print(b + 8)
   
   At the prompt the user entered: 8<br /><br />

1. &nbsp;

        x = float(input("Enter any number: "))
        y = bool(input("Enter a boolean value: "))
        z = False
        if (x < 100 and z):
           print("Condition 1 was True")
        elif(x < 100 or not z):
           print("Condition 2 was True")
        elif(x < 200 and y):
           print("Condition 3 was True")
        else:
           print("None of the conditions were True")
   
   At the first prompt the user entered: 143.8  
   At the second prompt the user entered: True<br /><br />

1. &nbsp;

        x = int(input("Enter an integer: "))
        for i in range(x):
           print(list(range(i)))
   
   At the prompt the user entered: 4<br /><br />

*Check your answers by typing this code into IDLE*

&nbsp;



## Problem #18
Write a program that asks the player for two adjectives, one animal, one verb, one preposition, and one object. Then your program will use the three inputs to output the following sentences:

```
The <adjective 1> <animal> <verb> <preposition> the <adjective 2> <object>.  
The <adjective 1> <animal> was no longer <adjective 1>.
```

For Example:

```
Enter an adjective: stubborn
Enter an adjective: smelly
Enter a verb(past tense): slept
Enter a preposition: in
Enter an animal: hippopotamus
Enter an object: shoe

The stubborn hippopotamus slept in the smelly shoe.
The stubborn hippopotamus was no longer stubborn.
```

[solution](practice_solutions#problem-18-solution)

&nbsp;



## Problem #19
Write a program that asks the user for three numbers and uses those numbers to calculate and display information about three types of shapes.

Your program should match the following: 

```
Please give me three numbers
A: ...
B: ...
C: ...

If you have a cube with height B, it's surface area will be X.XX and volume X.XX.

If you have a circle with diameter C, the radius will be X.XX, the circumference X.XX, and the area X.XX. 

If you have a triangle with height A and base B, the area will be X.XX.
```

*Note*: `...` represent user input and `X.XX` represent the calculated values.

The following formulas may be useful as you work on this program:
 
- Cubes
  - Surface area: \\(A = 6a^2\\) *(where \\(a\\) is the length of an edge)*
  - Volume: \\(V = a^3\\) 
- Circles
  - Diameter: \\(d = 2r\\) *(where \\(r\\) is the radius)*
  - Circumference: \\(C = \pi d\\) 
  - Area: \\(A = \pi r^2\\) 
- Triangles
  - Area: \\(A = \frac{1}{2}hb\\) *(where \\(h\\) is the height and \\(b\\) is the base)*

[solution](practice_solutions#problem-19-solution)

&nbsp;
