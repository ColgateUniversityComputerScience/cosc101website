# problem 1
def problem1(s):
    print("1.", s[len(s)//2] )
    print("2.", s[:len(s)//2] )
    print("3.", s[len(s)//2+1:] )

# problem 2
def problem2(s='abcdefghij'):
    print("1.", s[-1::-1] )
    print("2.", s[0:len(s):3] )
    print("3.", s[-2::-2] )

# problem 3
def countsubstr(s, sub):
    count = 0
    for i in range(len(s)-len(sub)+1):
        slice = s[i:(i+len(sub))]
        if slice == sub:
            count += 1
    return count

# problem 4
def makeAcronym(phrase):
    acro = ''
    words = phrase.split()
    for w in words:
        acro += w[0].upper()
    return acro

# problem 5
def removeAs(s):
    newstr = ''
    for ch in s:
       if ch.lower() != 'a':
           newstr += ch
    return newstr

# problem 6
def arrange_names(names):
    name_list = names.split()
    name_list.sort()
    ordered_names = " ".join(name_list)
    return ordered_names

# problem 7
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

# problem 8
def is_anagram(s, t):
    '''check whether strings s and t are anagrams of
       each other'''
    # a one-liner to do it
    return sorted(list(s)) == sorted(list(t))

def is_anagram_loop(s, t):
    # another, slightly more complicated way to do it
    for char in s:
        if s.count(char) != t.count(char):
            return False
    return True

def is_anagram_efficient(s, t):
    # the most time-efficient way to do it
    # (take COSC 102 for details!)
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

# Problem 9
def is_rotation(s, t):
    for i in range(len(s)):
        front = s[:i]
        back = s[i:]
        if back+front == t:
            return True
    return False

# Problem 10
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

#Problem 11
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

# Problem 12
def wordCount(filename, word):
    infile = open(filename)
    count = 0
    for line in infile:
        for w in line.split():
            if word.lower() == w.lower():
                count += 1
    infile.close()
    return count

# Problem 13
def averageLineLength(filename):
    numlines = 0
    charcount = 0
    infile = open(filename)
    for line in infile:
        numlines += 1
        charcount += len(line)
    infile.close()
    return charcount / numlines

# Problem 14
def biggest_difference():
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
    print(bdsymbol,"had the biggest difference:",bigdiff)

# Problem 15
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

# Problem 16
def countevens(lst):
    count = 0
    for val in lst:
        if val % 2 == 0:
            count += 1
    return count

# Problem 17
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

# Problem 18
def sumSquares(x):
    sum = 0
    for val in x:
        sum += val ** 2
    return sum

# Problem 19
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

# Problem 20
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

# Problem 21
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

# Problem 22
def sumOddsLt7(mylist):
    s = 0
    for value in mylist:
        if value % 2 == 1 and value < 7:
            s += value
    return s

# Problem 23
def removeOddsLe7(mylist):
    newlist = []
    for value in mylist:
        if value % 2 == 0 and value <= 7:
            newlist.append(value)
    return newlist

# Problem 24
def secondLargest(mylist):
    largest = max(mylist)
    tmplist = []
    for value in mylist:
        if value != largest:
            tmplist += [value]
    return max(tmplist)

def secondLargest_v2(mylist):
    largest = max(mylist)
    second = min(mylist)
    for value in mylist:
        if second < value < largest:
            second = value
    return second

# Problem 25
def fractionsmaller(lst, x):
    lst = sorted(lst)
    n = len(lst)
    i = 0
    while i < n and x > lst[i]:
        i += 1
    return i/n

# Problem 26
def mystery1(xlist):
    while len(xlist) > 3:
        xlist.remove(max(xlist))

def problem26():
    mylist = [ 42, 5, 10, 6, 7, 10, 4 ]
    mystery1(mylist)
    print (mylist)

# Problem 27
def mystery3(i, list1, list2):
    i = i + 4
    list1[-1] = 42
    list2 = list1

def problem27():
    i = 2
    one = [4, 10]
    two = [-1, -1]
    mystery3(i, one, two)
    print(i)
    print(one)
    print(two)
