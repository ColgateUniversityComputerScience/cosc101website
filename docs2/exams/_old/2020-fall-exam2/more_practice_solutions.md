---
title: COSC 101&#58; Exam 2 More Practice Problem Solutions
---

Download the code for these solutions: [more_practice.py](more_practice.py)



## Problem #1 Solution
[problem description](more_practice_problems#problem-1)

  1. `print( s[len(s)//2] )`

  2. `print( s[:len(s)//2] )`

  3. `print( s[len(s)//2+1:] )`

&nbsp;


## Problem #2 Solution
[problem description](more_practice_problems#problem-2)

  1. `print( s[-1::-1] )`

  2. `print( s[0:len(s):3] )`

  3. `print( s[-2::-2] )`

&nbsp;


## Problem #3 Solution
[problem description](more_practice_problems#problem-3)

```python
def countsubstr(s, sub):
    count = 0
    for i in range(len(s)-len(sub)+1):
        slice = s[i:(i+len(sub))]
        if slice == sub:
            count += 1
    return count
```

&nbsp;


## Problem #4 Solution
[problem description](more_practice_problems#problem-4)

```python
def makeAcronym(phrase):
    acro = ''
    words = phrase.split()
    for w in words:
        acro += w[0].upper()
    return acro
```

&nbsp;


## Problem #5 Solution
[problem description](more_practice_problems#problem-5)

```python
def removeAs(s):
    newstr = ''
    for ch in s:
       if ch.lower() != 'a':
           newstr += ch
    return newstr
```

&nbsp;


## Problem #6 Solution
[problem description](more_practice_problems#problem-6)

```python
def arrange_names(names):
    name_list = names.split()
    name_list.sort()
    ordered_names = " ".join(name_list)
    return ordered_names
```

&nbsp;


## Problem #7 Solution
[problem description](more_practice_problems#problem-7)

```python
def unique_letters(word):
    result = ''
    for char in word:
        if char not in result:
            result += char
    return result

def guess_letters(word):
    word = unique_letters(word).upper()
    guesses = 0
    correct = []
    incorrect = []
    while len(correct) < len(word):
        if correct != []:
            print("Correct Letters:   ", ", ".join(correct))
        if incorrect != []:
            print("Incorrect Letters: ", ", ".join(incorrect))
        print(len(word)-len(correct), "letters to be guessed")

        guess = input('\nGuess a letter: ').upper()       
        if len(guess) == 1:
            guesses += 1
            if guess in word and guess not in correct:
                print("Good guess!\n")
                correct.append(guess)
            elif guess not in word and guess not in incorrect:
                print("Nope.\n")
                incorrect.append(guess)
            else:
                print("You already guessed "+guess+"!\n")

        elif guess == 'QUIT' or guess == 'EXIT' or guess == 'I GIVE UP!':
            print('You give up? Okay, the word was "'+word+'".')
            return guesses

        else:  
            print("Enter only one letter at a time.")

    return guesses
```

&nbsp;


## Problem #8 Solution
[problem description](more_practice_problems#problem-8)

This program can be written in a single line!

```python
def is_anagram(s, t):
    return sorted(list(s)) == sorted(list(t))
```

This solution uses a for loop:

```python
def is_anagram_loop(s, t):
    for char in s:
        if s.count(char) != t.count(char):
            return False
    return True
```

The most time-efficient solution: (take COSC 102 for details!)

```python
def is_anagram_efficient(s, t):
    if len(s) != len(t):
        return False
    s_letters = {}
    for ch in s:
        if ch not in s_letters:
            s_letters[ch] = 1
        else:
            s_letters[ch] += 1
    for ch in t:
        if ch not in s_letters or s_letters[ch]==0:
            return False
        else:
            s_letters[ch] -= 1
    return True
```

&nbsp;


## Problem #9 Solution
[problem description](more_practice_problems#problem-9)

```python
def is_rotation(s, t):
    for i in range(len(s)):
        front = s[:i]
        back = s[i:]
        if back+front == t:
            return True
    return False
```

&nbsp;


## Problem #10 Solution
[problem description](more_practice_problems#problem-10)

```python
def maxStock(filename):
    maxval = -1
    symbol = ''
    infile = open(filename)
    for line in infile:
        fields = line.split()
        if float(fields[1]) > maxval:
            symbol = fields[0]
            maxval = float(fields[1])
    infile.close()
    return symbol
```

&nbsp;


## Problem #11 Solution
[problem description](more_practice_problems#problem-11)

```python
def findeees(filename):
    inf = open(filename)
    elist = []
    for line in inf:
        words = line.split()
        for word in words:
            ecount = 0
            for ch in word:
                if ch == 'e':
                    ecount += 1
            if ecount >= 3:
                elist.append(word)
    inf.close()
    return elist
```

&nbsp;


## Problem #12 Solution
[problem description](more_practice_problems#problem-12)

```python
def wordCount(filename, word):
    infile = open(filename)
    count = 0
    for line in infile:
        for w in line.split():
            if word.lower() == w.lower():
                count += 1
    infile.close()
    return count
```

&nbsp;


## Problem #13 Solution
[problem description](more_practice_problems#problem-13)

```python
def averageLineLength(filename):
    numlines = 0
    charcount = 0
    infile = open(filename)
    for line in infile:
        numlines += 1
        charcount += len(line)
    infile.close()	   
    return charcount / numlines
```

&nbsp;


## Problem #14 Solution
[problem description](more_practice_problems#problem-14)

```python
infile = open('data.txt')
bigdiff = 0
bdsymbol = ''
for line in infile:
   symbol,low,high = line.split()
   diff = float(high) - float(low)
   if diff > bigdiff:
       bigdiff = diff
       bdsymbol = symbol
infile.close()
print(bdsymbol,"had the biggest  difference:",bigdiff)
```

&nbsp;


## Problem #15 Solution
[problem description](more_practice_problems#problem-15)

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

def median_of_list(thelist):
    thelist = sorted(thelist)
    n = len(thelist)
    if n % 2 == 1:
        return thelist[n//2]
    else:
        mid = n//2
        return (thelist[mid-1] + thelist[mid])/2

def median_of_file(filename):
    infile = open(filename)
    numberlist = []
    for line in infile:
        numberlist += process_line(line)
    infile.close()
    return median_of_list(numberlist)
```

&nbsp;


## Problem #16 Solution
[problem description](more_practice_problems#problem-16)

```python
def countevens(lst):
    count = 0
    for val in lst:
        if val % 2 == 0:
            count += 1
    return count
```

&nbsp;


## Problem #17 Solution
[problem description](more_practice_problems#problem-17)

```python
def sum67(lst):
    sum = 0
    ignore = False
    for val in lst:
        if val == 6:
            ignore = True

        if not ignore:
            sum += val

        if ignore and val == 7:
            ignore = False
    return sum
```

&nbsp;


## Problem #18 Solution
[problem description](more_practice_problems#problem-18)

```python
def sumSquares(x):
    sum = 0
    for val in x:
        sum += val ** 2
    return sum
```

&nbsp;


## Problem #19 Solution
[problem description](more_practice_problems#problem-19)

```python
def removeOdd1(mylist):
   '''
   Remove odd elements; don't modify the parameter list, just
   return a new list.
   '''
   newlist = []
   for value in mylist:
       if value % 2 == 0:
           newlist.append(value)
   return newlist
```

&nbsp;


## Problem #20 Solution
[problem description](more_practice_problems#problem-20)

```python
def removeOdd2(mylist):
    '''
    Remove odd elements from the list passed as a parameter.
    '''
    i = 0
    while i < len(mylist):
        if mylist[i] % 2 == 1:
            del mylist[i]
            # don't increment i when we remove
            # an element!
        else:
            i += 1
```

&nbsp;


## Problem #21 Solution
[problem description](more_practice_problems#problem-21)

```python
def mostFrequent(mylist):
    maxvals = [ mylist[0] ]
    maxcount = mylist.count(maxvals[0])
    for i in range(1,len(mylist)):
        thiscount = mylist.count(mylist[i])
        if thiscount == maxcount and mylist[i] not in maxvals:
            maxvals.append(mylist[i])
        elif thiscount > maxcount:
            maxvals = [ mylist[i] ]
            maxcount = thiscount
    return maxvals
```

&nbsp;


## Problem #22 Solution
[problem description](more_practice_problems#problem-22)

```python
def sumOddsLt7(mylist):
    s = 0
    for value in mylist:
        if value % 2 == 1 and value < 7:
            s += value
    return s
```

&nbsp;


## Problem #23 Solution
[problem description](more_practice_problems#problem-23)

```python
def removeOddsLe7(mylist):
    newlist = []
    for value in mylist:
        if value % 2 == 0 and value <= 7:
            newlist.append(value)
    return newlist
```

&nbsp;


## Problem #24 Solution
[problem description](more_practice_problems#problem-24)

```python
def secondLargest(mylist):
    largest = max(mylist)
    tmplist = []
    for value in mylist:
        if value != largest:
            tmplist += [value]
    return max(tmplist)
```
An alternate solution:

```python
def secondLargest_v2(mylist):
    largest = max(mylist)
    second = min(mylist)
    for value in mylist:
        if second < value < largest:
            second = value
    return second
```

&nbsp;


## Problem #25 Solution
[problem description](more_practice_problems#problem-25)

```python
def fractionsmaller(lst, x):
    lst = sorted(lst)
    n = len(lst)
    i = 0
    while i < n and x > lst[i]:
        i += 1
    return i/n
```

&nbsp;


## Problem #26 Solution
[problem description](more_practice_problems#problem-26)

```python
[5, 6, 4]
```

&nbsp;


## Problem #27 Solution
[problem description](more_practice_problems#problem-27)

```python
2
[4, 42]
[-1, -1]
```

&nbsp;


## Problem #28 Solution
[problem description](more_practice_problems#problem-28)

```
N = int(input("What is N? "))
for k in range(N+1):
    if k >= 2:
        divisors = 0
        for i in range(k):
            if k % (i+1) == 0:
                divisors = divisors + 1
        print (k,'has',divisors,'divisors')
```
