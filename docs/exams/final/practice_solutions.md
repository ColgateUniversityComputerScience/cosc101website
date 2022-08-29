---
title: COSC 101&#58; Final Exam Practice Problem Solutions
math: true
---

## Expression Problem Solutions

```python
>>> a = 'rain snow sleet'
>>> b = [a, 40, 21]
>>> c = { 21:'freezing', 40:'cold', 75:'warm', 97:'hot'}
```


### Expression 1 Solution
```
>>> '7' in str(c[3])
KeyError (because there is no key 3 in the dictionary c)
```

### Expression 2 Solution
```
>>> a[0::5]
rss
```

### Expression 3 Solution
```
>>> print( 'temp is ' + str(sum(b[1:])/len(b[1:])) )
temp is 30.5
```

### Expression 4 Solution
```
>>> ' or '.join([c[97], c[int('40')]])
'hot or cold'
```

### Expression 5 Solution
```
>>> x = list(c.values())
>>> x.sort()
>>> print( x[0], a[:len(c)] )
cold rain
```

### Expression 6 Solution
```
>>> c['hamilton'] = { 'mon':31, 'tue':45, 'wed':40 }
>>> print( c['hamilton']['tue'] )
45
```

## More Expression Problems Solution
[problem description](practice_problems#more-expression-problems)

  1. `False`

  2. `IndexError: list index out of range`

  3. `doc`

  4. `True`

  5. `False`

  6. `AttributeError: 'NoneType' object has no attribute 'sort'`

  7. `3`

  8. `False`


&nbsp;



<!--
## Class Solutions

### Class 1 Solution
Write a class for getting/printing input using a class. [[Full description](practice_problems#class-problem-1)]

```python
class InputOutString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print( self.s.upper() )

strObj = InputOutString()
strObj.get_string()
strObj.print_string()
```


### Class 2 Solution
Write a kangaroo class including `put_in_pouch` and `pouch_contents` methods.  [[Full description](practice_problems#class-problem-2)]

```python
class Kangaroo:
    """a Kangaroo is a marsupial"""

    def __init__(self):
        """initialize the pouch contents; the default value is
        an empty list"""
        self.pouch_contents = []

    def __str__(self):
        """return a string representation of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = ["Pouch contents:" ]
        if len(self.pouch_contents) == 0:
            t.append("    No contents found.")
        for obj in self.pouch_contents:
            t.append('    ' + object.__str__(obj))
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
print( kanga )
print( roo )
```


### Class 3 Solution
Write a program to get circle radiuses and output circumferences and total area, using a circle class. [[Full description](practice_problems#class-problem-3)]

```python
import math

class Circle:
    def __init__(self):
        self.radius = 0
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius
    def get_area(self):
        return math.pi * (self.radius ** 2)
    def get_circumference(self):
        return 2 * math.pi * self.radius

def circle_areas():
    area = 0
    i = 1
    prompt = "Please enter the radius of a circle, or 'Done' to exit: "
    response = input(prompt).lower()
    while response != 'done':
        try:
            circle = Circle()
            radius = float(response)
            circle.set_radius(radius)
            area += circle.get_area()
            print( "The circumference of circle "+str(i)+" is "+\
                   str(circle.get_circumference())+".\n" )
            i += 1
            response = input(prompt).lower()
        except ValueError:
            print( "You did not enter a valid number or the word 'Done'"+\
                   ", please try again.\n")
    print( "\nThe total area of the "+str(i)+" circles you entered is "+\
           str(area)+".")

circle_areas()
```

### Class 4 Solution
Write a program that asks the user for point coordinates and displays the coordinates of the centroid point using the `Point` class from the textbook and the three specified methods. [[Full description](practice_problems#class-problem-4)]

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

def get_points():
    points = []
    prompt = "Would you like to create a point? (y/n) "
    prompt_x = "   x: "
    prompt_y = "   y: "
    another = input(prompt).lower()
    while another != "n":
        try:
            x = int(input(prompt_x))
            y = int(input(prompt_y))
            points.append(Point(x, y))
        except ValueError:
            print( "   Invalid coordinates, please try again. \n"+\
                   "   Note: Only whole numbers are accepted." )
        print()
        another = input(prompt).lower()
    return points

def calculate_centroid(points):
    if points == []:
        return None
    sum_x = 0
    sum_y = 0
    for point in points:
        sum_x += point.getX()
        sum_y += point.getY()
    return Point( sum_x/len(points), sum_y/len(points) )

def main():
    points = get_points()
    num = len(points)
    if num > 0:
        centroid = calculate_centroid(points)
        print( "\n\nThe centroid of the " + str(num) + \
            " points you entered is " + str(centroid) + "." )
    else:
        print( "\n\nYou did not enter any points." )

main()
```
-->



## Recursion Solutions


### Recursion 1 Solution
Write a function that computes the Greatest Common Divisor between two numbers. [[Full description](practice_problems#recursion-problem-1)]

#### Recursion 1a Solution
While loop version

```python
def gcd(a,b):
  if b > a:
      a,b = b,a  #swap if out of order
  while b != 0:
      a,b = b,a%b
  return a

print( gcd(42,14) )
print( gcd(35,15) )
print( gcd(99,6) )
```


#### Recursion 1b Solution
Recursive version

```python
def recursive_gcd(a,b):
  if b > a:
      a,b = b,a  #swap if out of order
  if b == 0:
      return a
  else:
      return gcd(b, a%b)

print( recursive_gcd(42,14) )
print( recursive_gcd(35,15) )
print( recursive_gcd(99,6) )
```


### Recursion 2 Solution
Write a function called `recursiveLetterCount(s, c)` that recursively counts the number of occurrences of `c` in `s`. [[Full description](practice_problems#recursion-problem-2)]

```python
def recursiveLetterCount(s, c):
    # base case: if we've got a zero-length string,
    # count is (obviously) zero.
    if len(s) == 0:
        return 0
    else:
        # if first character is what we're looking for,
        # count is 1 plus however many c's we find in the
        # rest of the string.  otherwise, it is 0 plus
        # however many c's we find in the rest of the string.
        if s[0] == c:
            return 1 + recursiveLetterCount(s[1:], c)
        else:
            return recursiveLetterCount(s[1:], c)

print( recursiveLetterCount('madeline', 'e') )
print( recursiveLetterCount('computer science', 'e') )
print( recursiveLetterCount('', 'e') )
```


### Recursion 3 Solution
Write a recursive function that takes a list of integers as a parameter and recursively computes and returns the sum of the list. [[Full description](practice_problems#recursion-problem-3)]

```python
def recursiveSum(mylist):
    if len(mylist) == 0:
        return 0
    else:
        return mylist[0] + recursiveSum(mylist[1:])

print( recursiveSum([1,2,3,4]) )
```


### Recursion 4 Solution
Write a recursive function `rpow(a,b)` that computes and returns $$a^b$$, without using the `**` operator. [[Full description](practice_problems#recursion-problem-4)]

```python
def rpow(a,b):
    if b == 0:
        return 1
    return a * rpow(a,b-1)

print( rpow(6, 1) )
print( rpow(6, 2) )
print( rpow(6, 3) )
```


### Recursion 5 Solution
Write a recursive function to print out the digits of a number in English. [[Full description](practice_problems#recursion-problem-5)]

```python
def english_digits(n):
    numbers = ['zero','one','two','three','four',
               'five','six','seven','eight','nine']
    if n < 10:
        print( numbers[int(n)], end=" ")
    else:
        leftdigits = n // 10
        rightdigit = n % 10
        english_digits(leftdigits)
        print( numbers[int(rightdigit)], end=" ")

english_digits(1234)
```


### Recursion 6 Solution
Write a function called `removeNonLetters(s)` that takes one string and returns a new string in which all the non-letters in the original string are removed. [[Full description](practice_problems#recursion-problem-6)]

#### Recursion 6a Solution
While loop version

```python
def removeNonLetters(s):
    i = 0
    newstr = ''
    while i < len(s):
        if 'a' <= s[i].lower() <= 'z':
            newstr += s[i]
        i += 1
    return newstr

print( removeNonLetters('!@#asd$% $%sfg^&') )
```

### Recursion 6b Solution
Recursive version

```python
def removeNonLettersR(s):
    if len(s) == 0:
        return ''
    c = s[0]
    if 'a' <= c.lower() <= 'z':
        return c + removeNonLettersR(s[1:])
    else:
        return '' + removeNonLettersR(s[1:])

print( removeNonLettersR('!@#asd$% $%sfg^&') )
```


### Recursion 7 Solution
Write a function that takes a string named `original` as a parameter and produces a list of strings that contains all permutations of the characters in the `original` string. [[Full description](practice_problems#recursion-problem-7)]

```python
def generate_permutations(original):
    '''generate all permutations of the characters in original; return
       the permutations as a list.'''

    # permutation of a single character is just the character itself
    if len(original) <= 1:
        return original

    result = []

    # go through each character and generate permutations that
    # start with that character.
    for startidx in range(len(original)):
        # split string into character at startidx, and all the other characters
        startchar = original[startidx]
        sublist = generate_permutations(original[:startidx] + original[(startidx+1):])

        # sublist contains the permutations of the remaining characters
        # in the string.  concatenate the startchar with each of these
        # subpermutations.
        for substr in sublist:
            result.append(startchar + substr)

    return result

print( generate_permutations('ab') )
print( generate_permutations('abc') )
print( generate_permutations('abcdef')) # this makes a lot of output!
```

## Non-Recursive Problem Solutions

### Other 1 Solution
Write a function that returns the value of an investment at the end of a specified number of years. [[Full description](practice_problems#other-problem-1)]

```python
def future_value(principal, apr, years):
    for i in range(years):
        principal = principal * (1 + apr)
    return principal

print( future_value(1000, 0.004, 30) )
```


### Other 2 Solution
Write a function that computes the square root of the sum of squares of a given list. [[Full description](practice_problems#other-problem-2)]

```python
import math

def l2norm(mylist):
    sum = 0.0
    for v in mylist:
        sum += v ** 2
    return math.sqrt(sum)

print( l2norm([2,3,4]) )
```


### Other 3 Solution
[[Full program](practice_problems#other-problem-3)]
```
>>> mylist = [ 42, 5, 10, 6, 7, 10, 4 ]
>>> mystery1(mylist)
>>> print( mylist )
[5, 6, 4]
```


### Other 4 Solution
[[Full program](practice_problems#other-problem-4)]
```
>>> t = mystery2(3)
>>> print( t )
3
2
1
6
```


### Other 5 Solution
[[Full program](practice_problems#other-problem-5)]
```
>>> mystery3(i, one, two)
>>> print( i )
2
>>> print( one )
[4, 42]
>>> print( two )
[-1, -1]
```


### Other 6 Solution
Write a function `minTwo` that returns the smallest two unique elements in a list. [[Full description](practice_problems#other-problem-6)]

```python
def minTwo(mylist):
    newlist = sorted(mylist)
    index = 1
    while newlist[index] == newlist[0]:
        index += 1
    return newlist[0], newlist[index]

print( minTwo([5, 7, 10, 2, -1, 7, 3]) )
```


### Other 7 Solution
Write a function to estimate the value of $$\pi$$. [[Full description](practice_problems#other-problem-7)]

```python
import random

def throwdart():
    return 2*random.random()-1,2*random.random()-1

def inside(x,y):
    return x**2 + y**2 <= 1

def pidarts(n):
    h = 0
    for i in range(n):
        x,y = throwdart()
        if inside(x,y):
            h += 1
    pi = 4 * h / float(n)
    return pi

print( pidarts(3) )
```


### Other 8 Solution
Write a teen-to-adult translator with a dictionary of at least 5 translations. [[Full description](practice_problems#other-problem-8)]

```python
def teentoadult_translator(phrase):
    d = {
        'u':'you',
        'r':'are',
        'y':'why',
        'l8':'late',
        'omg':'oh my god',
        }

    newphraselist = []
    for word in phrase.strip().split():
        # just handle basic punctuation
        punctuation = ''
        if word[-1] in ['.','?','!',',']:
            punctuation = word[-1]
            word = word[:-1]
        translation = word
        if word in d:
            translation = d[word]
        if len(punctuation) > 0:
            translation += punctuation
        newphraselist.append(translation)
    return ' '.join(newphraselist)

print( teentoadult_translator("omg, i'm l8!") )
```


### Other 9 Solution
Write a function that takes one string and returns a list of all the unique characters in the string. [[Full description](practice_problems#other-problem-9)]

#### Other 9a Solution
Use only lists.

```python
def uniqueletters_list(s):
    s = s.lower()
    charlist = list(s)
    i = 0
    while i < len(charlist):
        letter = charlist[i]
        removed = False
        while charlist.count(letter) > 1:
            charlist.remove(letter)
            removed = True
        if not removed:
            i += 1
    return sorted(charlist)

print( uniqueletters_list('The quick brown fox jumps over the lazy dog.') )
```

#### Other 9b Solution
Use a dictionary.

```python
def uniqueletters_dict(s):
    s = s.lower()
    d = {}
    for char in s:
        # unconditionally put the char as a key in the dictionary.  we
        # rely on the fact that keys must be unique.  at the end of
        # doing this, the keys in the dict are necessarily the unique
        # letters in the string
        d[char] = 'anything'
    return sorted(d.keys())

print( uniqueletters_dict('The quick brown fox jumps over the lazy dog.') )
```


### Other 10 Solution
Write a function that takes two fractions and returns their sum. [[Full description](practice_problems#other-problem-10)]

```python
def add_fractions(a, b):
    denoma = a[1]
    denomb = b[1]

    # need to find least common multiple of da, db
    # for common denominator.  basically, need to
    # find da*db/gcd(da,db), where gcd is the greatest
    # common divisor.
    cd = (denoma * denomb) / gcd(denoma, denomb)

    numerator = (a[0] * (cd // a[1]) + b[0] * (cd // b[1]))
    return (numerator, cd)

print( add_fractions( (1,4), (1,4) ) )   
print( add_fractions( (1,2), (1,4) ) )
print( add_fractions( (2,3), (3,8) ) )
```


### Other 11 Solution
Write a function that shifts numbers in a list circularly to the left by the given amount. [[Full description](practice_problems#other-problem-11)]

```python
def shiftleft(mytuple, k):
    # simple approach: turn the tuple into a list
    mylist = list(mytuple)
    if k >= len(mylist):
        return
    # pretty simple with slicing; slicing makes
    # copy of list elements, so we're not modifing
    # the original list
    mylist = mylist[k:] + mylist[:k]
    return tuple(mylist)

print( shiftleft((1,2,3,4,5),2) )
```


### Other 12 Solution
Write a function that shifts numbers in a *tuple* circularly to the left by the given amount. [[Full description](practice_problems#other-problem-12)]

```python
def shiftleft_tup(mytuple, k):
    # simple approach: turn the tuple into a list
    mylist = list(mytuple)
    if k >= len(mylist):
        return
    # pretty simple with slicing; slicing makes
    # copy of list elements, so we're not modifing
    # the original list
    mylist = mylist[k:] + mylist[:k]
    return tuple(mylist)

print( shiftleft_tup((1,2,3,4,5),2) )
```


### Other 13 Solution
Write a function that reads a text file and finds pairs where lines contain the same string reversed and returns a list of those pairs as tuples. [[Full description](practice_problems#other-problem-13)]

```python
def findreversepairs(filename):
   infile = open(filename)
   d = {} # could use either a dictionary or list here
   for line in infile:
       word = line.strip()
       d[word] = 1
   d.close()
   wordpairs = []
   for key in d:
       reverseword = key[-1::-1]
       if reverseword in d:
           pair = (key,reverseword)
           wordpairs.append(pair)
   return wordpairs
```


### Other 14 Solution
Write a function that takes a list of strings and swaps the upper and lower case letters in the strings. [[Full description](practice_problems#other-problem-14)]

#### Recursive Helper Function
```
def swapcase(s):
    if len(s) == 0:
        return ''
    if 'A' <= s[0] <= 'Z':
        return s[0].lower() + swapcase(s[1:])
    else:
        return s[0].upper() + swapcase(s[1:])
```

#### Other 14a Solution
```
def swapcaselist_a(mylist):
    newlist = []
    for s in mylist:
        newlist.append(swapcase(s))
    return newlist

test_list = ['aPpLe', 'AAPL', 'gOOglE', 'goog']
print( swapcaselist_a(test_list) )
```

#### Other 14b Solution
```
def swapcaselist_b(mylist):
    for i in range(len(mylist)):
        mylist[i] = swapcase(mylist[i])

test_list = ['aPpLe', 'AAPL', 'gOOglE', 'goog']
swapcaselist_b(test_list)
print(test_list)
```


### Other 15 Solution
Write a function that returns a tuple containing the average and median of the numbers found in a file. [[Full description](practice_problems#other-problem-15)]

```python
def process_line(s):
    intlist = []
    for token in s.split():
        if '0' <= token[0] <= '9':
            i = 1
            while i < len(token) and '0' <= token[i] <= '9':
                i += 1
            intlist.append(int(token[:i]))
    return intlist

def average(thelist):
    return sum(thelist) / float(len(thelist))

def median(thelist):
    thelist = sorted(thelist)
    n = len(thelist)
    if n % 2 == 1:
        return thelist[int(n/2)]
    else:
        mid = int(n/2)
        return average([ thelist[mid-1], thelist[mid] ])

def avgmed(filename):
    infile = open(filename):
    numberlist = []
    for line in infile:
        numberlist += process_line(line)
    infile.close()
    return (average(numberlist), median(numberlist))
```


### Other 16 Solution
Write a spell checker function. [[Full description](practice_problems#other-problem-16)]

```python
def onlyalpha(s):
    '''return character up to but not including the first non-letter in the word'''
    news = ''
    i = 0
    while i < len(s) and s[i].isalpha():
        news += s[i]
        i += 1
    return news

def isvalid(word, validwords):
    '''binary search to check whether word is in the list of valid words.  this is a non-recursive version.'''
    low = 0
    high = len(validwords)-1
    while low < high:
        mid = (low + high) / 2
        if validwords[mid] == word:
            return True
        elif validwords[mid] < word:
            low = mid+1
        else:
            high = mid-1
    return False

def spell_check(filename, validwords):
    invalid_words = []
    infile = open(filename):    
    for line in infile:
        for word in line.split():
            word = onlyalpha(word)
            if not isvalid(word.lower(), validwords):
                invalid_words.append(word)
    infile.close()
    return invalid_words
```


### Other 17 Solution
You are creating a competitor to Facebook. [[Full description](practice_problems#other-problem-17)]

#### Other 17a Solution
Write a function that takes a friendship dictionary and returns the user with the most friends.

```python
def mostfriends(friendict):
    dsu = []
    for user,friendlist in friendict.items():
        dsu.append( (len(friendlist), user) )
    dsu.sort()
    return dsu[-1][1]
```

#### Other 17b Solution
Write a function that takes a friendship dictionary and username and returns the list of users that friends of the user's friends.

```python
def friendsoffriends(friendict, user):
    userlist = friendict[user]
    foflist = []
    for friend in userlist:
        for fof in friendict[friend]:
            if fof not in foflist and fof != user:
                foflist.append(fof)
    return foflist
```

## Other Problem #18 Solution
[problem description](practice_problems#other-problem-18)

```python
def is_subset(list1, list2):
    index = 0
    while index < len(list2):
      val = list2[index]
        if val not in list1:
            return False
        index += 1
    return True
```

&nbsp;


## Other Problem #19 Solution
[problem description](practice_problems#other-problem-19)

```python
def average_of_freeze_streak(templist):
    maxstreak = []
    streak = []
    inside = False
    index = 0
    while index < len(templist):
        if templist[index] <= 32:
            if not inside:
                inside = True
                streak = []
            streak += [ templist[index] ]
        else:
            if inside:
                if len(streak) > len(maxstreak):
                    maxstreak = streak
                inside = False
        index += 1

    if inside:
        if len(streak) > len(maxstreak):
            streak = maxstreak

    if len(maxstreak) > 0:
        return sum(maxstreak)/float(len(maxstreak))
    return None
```

&nbsp;


## Other Problem #20 Solution
[problem description](practice_problems#other-problem-20)

```python
def one_string(s, char):
    i = 0
    count = 0
    while i < len(s):
        if s[i] == char:
            count += 1
        i += 1
    return count

def count_chars(stringlist, char):
    i = 0
    count = 0
    while i < len(stringlist):
        count += one_string(stringlist[i], char)
        i += 1
    return count
```

&nbsp;


## Other Problem #21 Solution
[problem description](practice_problems#other-problem-21)

```python
def unique_chars(s):
    chars = []
    i = 0
    while i < len(s):
        if s[i] in chars:
            return False
        chars = chars + [ s[i] ]
        i += 1
    return True
```

&nbsp;


## Other Problem #22 Solution
[problem description](practice_problems#other-problem-22)

```python
def numBefore(s, c):
    count = 0
    index = 0
    while index < len(s):
        if s.lower()[index] < c.lower():
            count += 1
        index += 1
    return count
```

&nbsp;


<!-- The following are the problems moved from Exam 3 review during spring 2020 when we lost of a week of classes and pushed dictionaries to the final exam -->

## Other Problem #23 Solution
[problem description](practice_problems#other-problem-23)

1. 

```python
def most_friends(friendict):
    dsu = []
    for user,friendlist in friendict.items():
        dsu.append( [len(friendlist), user] )
    dsu.sort()
    return dsu[-1][1]
```

2. 

```python
def friends_of_friends(friendict, user):
    userlist = friendict[user]
    foflist = []
    for friend in userlist:
        for fof in friendict[friend]:
            if fof not in foflist and fof != user:
                foflist.append(fof)
    return foflist
```

&nbsp;

## Other Problem #24 Solution
[problem description](practice_problems#other-problem-24)

```python
def teentoadult_translator(phrase):
    d = { 
        'u':'you',
        'r':'are',
        'y':'why',
        'l8':'late',
        'omg':'oh my god',
        }

    newphraselist = []
    for word in phrase.strip().split():
        # just handle basic punctuation
        punctuation = ''
        if word[-1] in ['.','?','!',',']:
            punctuation = word[-1]
            word = word[:-1]
        translation = word
        if word in d:
            translation = d[word]
        if len(punctuation) > 0:
            translation += punctuation
        newphraselist.append(translation)
    return ' '.join(newphraselist)
```

&nbsp;


## Other Problem #25 Solution
[problem description](practice_problems#other-problem-25)

```python
def uniqueletters_dict(s):
    d = {}
    for char in s:
        # unconditionally put the char as a key in the dictionary.  we
        # rely on the fact that keys must be unique.  at the end of
        # doing this, the keys in the dict are necessarily the unique
        # letters in the string
        d[char] = 'anything'
    return sorted(d.keys())
```

&nbsp;


## Other Problem #26 Solution
[problem description](practice_problems#other-problem-26)

```python
def remove_if_more_than_k(lst, k):
    histo = {}
    for i in range(len(lst)):
        value = lst[i]
        if value in histo:
            histo[value] += 1
        else:
            histo[value] = 1

    # remove items, being careful about index access
    for value in histo:
        count = histo[value]
        if count > k:
            i = 0
            while i < len(lst):
                if lst[i] == value:
                    del lst[i]
                else:
                    i += 1
```

&nbsp;