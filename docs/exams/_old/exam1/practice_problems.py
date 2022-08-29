### Problem 4
##years = int(input("years: "))
##pop = 307357870
##secs = years * 365 * 24 * 60 * 60
##births = secs / 7
##deaths = secs / 13
##newimmigrants = secs / 35
##print ( int(pop + births - deaths + newimmigrants) )

### Problem 5
##N = int(input("What is N? "))
##sum = 0
##for i in range(N):
##    sum = sum + (i+1)
##print(sum)

### Problem 6
##N = int(input("What is N? "))
##sum = 0
##for i in range(N):
##    sum = sum + (i+1)
##    print(sum)

### Problem 7
##knuts = int(input("How many knuts? "))
##sickles = knuts // 29
##if sickles > 0:
##    galleons = sickles // 17
##    # compute the remaining sickles
##    sickles = sickles % 17
##    if galleons > 0:
##        print ("There are",int(galleons),"galleons.")
##    if sickles > 0:
##        print ("There are",int(sickles),"sickles.")

### Problem 8
##i = int(input('gimme an int: '))
##if i % 2 == 0:
##    print('even')
##else:
##    print('odd')
##if i % 4 == 0 and i % 7 == 0:
##    print('divisible by 4 and 7')


### Problem 9
##numdays =  int(input("How many days did it snow? "))
##totalsnow = 0
##maxsnow = 0
##for i in range(numdays):
##    snowamt = int(input("Enter snowfall amount: "))    
##    totalsnow = totalsnow + snowamt
##    if snowamt > maxsnow:
##        maxsnow = snowamt
##snowavg = totalsnow / 28.0 
##print("The average snowfall per day is",snowavg,"cm.")
##print("The maximum daily snowfall is",maxsnow,"cm.")


### Problem 11
##secs = int(input("What's the number of seconds (1-86400)? "))
##hours = secs // (60*60) # integer division!
##secs = secs - hours*60*60
##mins = secs // 60  # again, integer division
##secs = secs % 60
##print (str(int(hours))+":"+str(int(mins))+":"+str(int(secs)))


### Problem 12
##N = int(input("What is N? "))
##for k in range(N+1):
##    if k >= 2:
##        divisors = 0
##        for i in range(k):
##            if k % (i+1) == 0:
##                divisors = divisors + 1
##        print (k,'has',divisors,'divisors')


### Problem 13
##principal = float(input("How much is the initial investment? "))
##rate = float(input("What is the interest rate? "))
##years = int(input("How many years to invest? "))
##totinterest = 0.0
##
### in the print statements below, the \t is a tab character; it just helps with spacing.
### you could just use spaces, too, or anything else that spaces things out nicely.
##
##print("Year\tTotal investment value\tInterest earned")
##print("----\t----------------------\t---------------")
##print(0,"\t",round(principal,2),"\t\t\t",round(totinterest,2))
##for i in range(years):
##    interest = principal * rate
##    totinterest = totinterest + interest
##    principal = principal + interest
##    if principal < 10000: # extra tab needed for alignment
##        print(i+1,"\t",round(principal,2),"\t\t\t",round(totinterest,2))
##    else:                 # no extra tab necessary
##        print(i+1,"\t",round(principal,2),"\t\t",round(totinterest,2))
##
##

### Problem 14 v1
### Wallis approximation to pi, version 1
### This version uses a for loop over pairs
### of terms in the product
##terms = int(input("How many terms? "))
##pi = 2.0
##for pair in range(terms//2):
##    num = 2 * pair + 2
##    denom = 2 * pair + 1
##    pi = pi * num / denom
##    denom = denom + 2
##    pi = pi * num / denom
##
##print("The pi approximation is", pi)

### Problem 14 v2
### Wallis approximation to pi, version 2
### This version uses a for loop plus an
### if statement to adjust for odd/even terms
##terms = int(input("How many terms? "))
##pi = 2.0
##for term in range(terms):
##    if term % 2 == 0:
##        num = term + 2
##        denom = term + 1
##    else:
##        num = term + 1
##        denom = term + 2
##    pi = pi * num / denom
##
##print("The pi approximation is", pi)

### Problem 15
##therange = 56-10
##for i in range(therange+1):
##    if (i+10) % 6 == 0:
##        print(i+10)


### Problem 16
##n = int(input("What number to test for primality? "))
##isprime = True
##for i in range(2, n):	# really only need range(2, int(n**0.5)+1)
##    if n % i == 0:
##        isprime = False
##if isprime:
##    print(n,"is prime")
##else:
##    print(n,"is not prime")


### Problem 18
##adj1 = input("Enter an adjective: ")
##adj2 = input("Enter an adjective: ")
##verb = input("Enter a verb (past tense): ")
##prep = input("Enter a preposition: ")
##anim = input("Enter an animal: ")
##obje = input("Enter an object: ")
##
##print("\nThe", adj1, anim, verb, prep, "the", adj2, obje+".")
##print("The", adj1, anim, "was no longer", adj1+".")

## Problem 19
##import math
##pi = math.pi
##
##print("Please give me three numbers")
##a = float(input("A: "))
##b = float(input("B: "))
##c = float(input("C: "))
##
##cube_area = str(round(6 * b**2 , 2))
##cube_volume = str(round(b**3 , 2))
##print("If you have a cube with height B, it's surface area will be "+\
##      str(cube_area)+" and volume "+str(cube_volume)+".")
##
##circle_radius = round(c / 2 , 2)
##circle_circumference = round(pi * c , 2)
##circle_area = round(pi * circle_radius ** 2 , 2)
##print("If you have a circle with diameter C, the radius will be "+\
##      str(circle_radius)+', the circumference '+str(circle_circumference)+\
##      ', and the area '+str(circle_area)+'.')
##
##triangle_area = round((1/2) * b * a , 2)
##print('If you have a triangle with height A and base B, the area will be'+\
##      str(triangle_area)+'.')
           
