---
title: COSC 101&#58; Exam 2 Practice Problem Solutions
---

## Problem #1 Solution
[problem description](practice_problems#problem-1)

```
def multiplication_table(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            product = i * j
            print(product, end=" ")
        print()
```


&nbsp;

## Problem #2 Solution
[problem description](practice_problems#problem-2)

(a)

```
outer 2
inner 3
other 2
```

(b)

```
inner = 0
outer = 0
other = 0
ii = 1
while ii < 3:
    outer += 1
    other += ii
    jj = 1
    while jj > -ii:
        inner += 1
        other -= jj
        jj -= 2
    ii += 1
print ('outer',outer)
print ('inner',inner)
print ('other',other)

```

&nbsp;


## Problem #3 Solution
[problem description](practice_problems#problem-3)

```
def investment_doubling(rate):
    principal = 1
    initial_principal = principal
    years = 0
    while principal < initial_principal * 2:
        principal = principal + principal * rate
        years += 1
    return years
```

&nbsp;

## Problem #4 Solution
[problem description](practice_problems#problem-4)

```
def hide_character(phrase, character):
    updated = ""
    for c in phrase:
        if c == character.upper() or c == character.lower():
            updated = updated + '*'
        else:
            updated = updated + c
    return updated
```


&nbsp;

## Problem #5 Solution
[problem description](practice_problems#problem-5)

```
def average_of_inputs():
    sum = n = 0
    done = False
    while not done:
        num = int(input("What's the next number? "))
        if num == -999:
            done = True
        else:
            sum += num
            n += 1
    if n > 0:
        return sum / float(n)
    return None
```


## Problem #6 Solution
[problem description](practice_problems#problem-6)

```
def unique_chars(s):
    chars = []
    for i in range(len(s)):
        if s[i] in chars:
            return False
        chars = chars + [ s[i] ]
    return True
```

&nbsp;

## Problem #7 Solution
[problem description](practice_problems#problem-7)

```
def translate_spaces(url):
    newurl = ''
    for i in range(len(url)):
        if url[i] == ' ':
            newurl += '%20'
        else:
            newurl += url[i]
    return newurl
```


&nbsp;

## Problem #8 Solution
[problem description](practice_problems#problem-8)
Both functions determine the longer string, but the first function prints the answer while the second function returns it. The second one can be used in an expression while the first one cannot; e.g., it is valid to write:

```
s = cmpTwo('alpha','beta') * 2
```

but not valid to write:

```
s = cmpOne('alpha','beta') * 2
```


&nbsp;

## Problem #9 Solution
[problem description](practice_problems#problem-9)

```
def cmpFirstLast(s):
    if s[0] < s[-1]:
        return True
    return False
```


&nbsp;

## Problem #10 Solution
[problem description](practice_problems#problem-10)

(a)

```
def numBefore(s):
    count = 0
    for index in range(len(s)):
        if s[index] < 'h':
            count += 1
    return count
```

(b)

```
def numBefore(s):
    count = 0
    index = 0
    while index < len(s):
        if s[index] < 'h':
            count += 1
        index += 1
    return count
```
