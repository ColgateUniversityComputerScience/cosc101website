# recursion problem 1a
def gcd(m,n):
    while m != 0:
        n,m = m,n%m
    return n
##print (gcd(42,14))
##print (gcd(35,15))
##print (gcd(99,6))

# recursion problem 1b
def recursive_gcd(m,n):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)
##print (recursive_gcd(42,14))
##print (recursive_gcd(35,15))
##print (recursive_gcd(99,6))

# recursion problem 2
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
##print( recursiveLetterCount('madeline', 'e') )
##print( recursiveLetterCount('computer science', 'e') )
##print( recursiveLetterCount('', 'e') )

# recursion problem 3
def recursiveSum(mylist):
    if len(mylist) == 0:
        return 0
    else:
        return mylist[0] + recursiveSum(mylist[1:])
##print( recursiveSum([1,2,3,4]) )

# recursion problem 4
def rpow(a,b):
    if b == 0:
        return 1
    return a * rpow(a,b-1)
##print( rpow(6, 1) )
##print( rpow(6, 2) )
##print( rpow(6, 3) )

# recursion problem 5
def english_digits(n):
    numbers = ['zero','one','two','three','four',
               'five','six','seven','eight','nine']
    if n < 10:
        print( numbers[int(n)], end=" ")
    else:
        leftdigits = n / 10
        rightdigit = n % 10
        english_digits(leftdigits)
        print( numbers[int(rightdigit)], end=" ")
##english_digits(1234)

# recursion problem 6a
def removeNonLetters(s):
    i = 0
    newstr = ''
    while i < len(s):
        if 'a' <= s[i].lower() <= 'z':
            newstr += s[i]
        i += 1
    return newstr
##print( removeNonLetters('!@#asd$% $%sfg^&') )


# recursion problem 6b
def removeNonLettersR(s):
    if len(s) == 0:
        return ''
    c = s[0]
    if 'a' <= c.lower() <= 'z':
        return c + removeNonLettersR(s[1:])
    else:
        return '' + removeNonLettersR(s[1:])
##print( removeNonLettersR('!@#asd$% $%sfg^&') )


# recursive problem 7
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
##print( generate_permutations('ab') )
##print( generate_permutations('abc') )
##print( generate_permutations('abcdef') )

# other problem 1
def future_value(principal, apr, years):
    for i in range(years):
        principal = principal * (1 + apr)
    return principal
##print( future_value(1000, 0.004, 30) )


# other problem 2
import math
def l2norm(mylist):
    sum = 0.0
    for v in mylist:
        sum += v ** 2
    return math.sqrt(sum)
##print( l2norm([2,3,4]) )


# other problem 3
def mystery1(xlist):
    while len(xlist) > 3:
        xlist.remove(max(xlist))

mylist = [ 42, 5, 10, 6, 7, 10, 4 ]
mystery1(mylist)
##print (mylist)


# other problem 4
def mystery2(n):
    if n == 0:
        return 0
    else:
        print (n)
        return n + mystery2(n-1)
##t = mystery2(3)
##print (t)


# other problem 5
def mystery3(i, list1, list2):
    i = i + 4
    list1[-1] = 42
    list2 = list1
i = 2
one = [4, 10]
two = [-1, -1]
mystery3(i, one, two)
##print (i)
##print (one)
##print (two)


# other problem 6
def minTwo(mylist):
    newlist = sorted(mylist)
    index = 1
    while newlist[index] == newlist[0]:
        index += 1
    return newlist[0], newlist[index]
##print( minTwo([5, 7, 10, 2, -1, 7, 3]) )


# other problem 7
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
##print( pidarts(3) )


# other problem 8
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
##print( teentoadult_translator("omg, i'm l8!") )


# other problem 9a solution
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
##print( uniqueletters_list('The quick brown fox jumps over the lazy dog.') )

# other problem 9b solution
def uniqueletters_dict(s):
    s = s.lower()
    d = {}
    for char in s:
        d[char] = 'anything'
    return sorted(d.keys())
##print( uniqueletters_dict('The quick brown fox jumps over the lazy dog.') )


# other problem 10
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
##print( add_fractions( (1,4), (1,4) ) )
##print( add_fractions( (1,2), (1,4) ) )
##print( add_fractions( (2,3), (3,8) ) )


# other problem 11
def shiftleft(mylist, k):
    if k >= len(mylist):
        return
    # pretty simple with slicing; slicing makes
    # copy of list elements, so we're not modifing
    # the original list
    return mylist[k:] + mylist[:k]
##print( shiftleft([1,2,3,4,5],2) )


# other problem 12
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
##print( shiftleft_tup((1,2,3,4,5),2) )


# other problem 13
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

# other problem 14
def swapcase(s):
    if len(s) == 0:
        return ''
    if 'A' <= s[0] <= 'Z':
        return s[0].lower() + swapcase(s[1:])
    else:
        return s[0].upper() + swapcase(s[1:])
def swapcaselist_a(mylist):
    newlist = []
    for s in mylist:
        newlist.append(swapcase(s))
    return newlist
def swapcaselist_b(mylist):
    for i in range(len(mylist)):
        mylist[i] = swapcase(mylist[i])
##test_list = ['aPpLe', 'AAPL', 'gOOglE', 'goog']
##print( swapcaselist_a(test_list) )
##swapcaselist_b(test_list)
##print(test_list)


# other problem 15 solution
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
        return thelist[n/2]
    else:
        mid = n/2
        return average([ thelist[mid-1], thelist[mid] ])
def avgmed(filename):
    infile = open(filename)
    numberlist = []
    for line in infile:
        numberlist += process_line(line)
    infile.close()
    return (average(numberlist), median(numberlist))

###
### class problem 3
##import math
##class Circle:
##    def __init__(self):
##        self.radius = 0
##    def get_radius(self):
##        return self.radius
##    def set_radius(self, new_radius):
##        self.radius = new_radius
##    def get_area(self):
##        return math.pi * math.sqrt(self.radius)
##    def get_circumference(self):
##        return 2 * math.pi * self.radius
##def circle_areas():
##    area = 0
##    i = 1
##    prompt = "Please enter the radius of a circle, or 'Done' to exit: "
##    response = input(prompt).lower()
##    while response != 'done':
##        try:
##            circle = Circle()
##            radius = float(response)
##            circle.set_radius(radius)
##            area += circle.get_area()
##            print( "The circumference of circle "+str(i)+" is "+\
##                   str(circle.get_circumference())+".\n" )
##            i += 1
##            response = input(prompt).lower()
##        except ValueError:
##            print( "You did not enter a valid number or the word 'Done'"+\
##                   ", please try again.\n")
##    print( "\nThe total area of the "+str(i)+" circles you entered is "+\
##           str(area)+".")
####circle_areas()
##
##
##
### class problem 2
##class Kangaroo:
##    """a Kangaroo is a marsupial"""
##
##    def __init__(self):
##        """initialize the pouch contents; the default value is
##        an empty list"""
##        self.pouch_contents = []
##
##    def __str__(self):
##        """return a string representation of this Kangaroo and
##        the contents of the pouch, with one item per line"""
##        t = [ object.__str__(self) + "'s pouch contents:" ]
##        if len(self.pouch_contents) == 0:
##            t.append("    No contents found.")
##        for obj in self.pouch_contents:
##            s = '    ' + object.__str__(obj)
##            t.append(s)
##        return '\n'.join(t)
##
##    def put_in_pouch(self, item):
##        """add a new item to the pouch contents"""
##        self.pouch_contents.append(item)
####kanga = Kangaroo()
####roo = Kangaroo()
####kanga.put_in_pouch('wallet')
####kanga.put_in_pouch('car keys')
####kanga.put_in_pouch(roo)
####print( kanga )
####print( roo )
##
##
### class problem 4 solution
##class Point:
##
##    def __init__(self, initX, initY):
##        """ Create a new point at the given coordinates. """
##        self.x = initX
##        self.y = initY
##
##    def getX(self):
##        return self.x
##
##    def getY(self):
##        return self.y
##
##    def distanceFromOrigin(self):
##        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
##
##    def __str__(self):
##        return "x=" + str(self.x) + ", y=" + str(self.y)
##
##    def halfway(self, target):
##        mx = (self.x + target.x) / 2
##        my = (self.y + target.y) / 2
##        return Point(mx, my)
##def get_points():
##    points = []
##    prompt = "Would you like to create a point? (y/n) "
##    prompt_x = "   x: "
##    prompt_y = "   y: "
##    another = input(prompt).lower()
##    while another != "n":
##        try:
##            x = int(input(prompt_x))
##            y = int(input(prompt_y))
##            points.append(Point(x, y))
##        except ValueError:
##            print( "   Invalid coordinates, please try again. \n"+\
##                   "   Note: Only whole numbers are accepted." )
##        print()
##        another = input(prompt).lower()
##    return points
##def calculate_centroid(points):
##    if points == []:
##        return None
##    sum_x = 0
##    sum_y = 0
##    for point in points:
##        sum_x += point.getX()
##        sum_y += point.getY()
##    return Point( sum_x/len(points), sum_y/len(points) )
##def centroid_main():
##    points = get_points()
##    num = len(points)
##    if num > 0:
##        centroid = calculate_centroid(points)
##        print( "\n\nThe centroid of the " + str(num) + \
##            " points you entered is " + str(centroid) + "." )
##    else:
##        print( "\n\nYou did not enter any points." )
####centroid_main()
