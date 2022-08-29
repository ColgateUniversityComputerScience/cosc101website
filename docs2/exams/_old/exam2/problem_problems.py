#problem 1
def multiplication_table(n):
    i = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            product = i * j
            print (product, end=" ")
            j += 1
        print()
        i += 1

#problem 2
def nested_for():
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

def nested_while():
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


#problem 3
def investment_doubling(rate):
    principal = 1
    initial_principal = principal
    years = 0
    while principal < initial_principal * 2:
        principal = principal + principal * rate
        years += 1
    return years


#problem 4
def countOdd(x):
    count = 0
    for val in x:
        if val % 2 == 1:
            count += 1
    return count


#problem 5
def half_evens(integer_list):
   newlist = []
   for value in integer_list:
       if value % 2 == 0:
           newlist += [ value//2 ]
   return newlist


#problem 6
def sumSquares(x):
   sum = 0
   for val in x:
       sum += val ** 2
   return sum


#problem 7
def is_subset(list1, list2):
    for index in range(len(list2)):
        val = list2[index]
        if val not in list1:
            return False
    return True


#problem 8
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


#problem 9
def average_of_freeze_streak(templist):
    maxstreak = []
    streak = []
    inside = False
    for index in range(len(templist)):
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

    if inside:
        if len(streak) > len(maxstreak):
            streak = maxstreak

    if len(maxstreak) > 0:
        return sum(maxstreak)/float(len(maxstreak))
    return None


#problem 10
def one_string(s, char):
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count += 1
    return count

def count_chars(stringlist, char):
    count = 0
    for i in range(len(stringlist)):
        count += one_string(stringlist[i], char)
    return count


#problem 11
def swap(mylist, i, j):
    temp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = temp

def bubble(mylist):
    for i in range(len(mylist) - 1):
        if mylist[i] > mylist[i+1]:
            swap(mylist, i, i+1)

def run_11():
    mylist = [3,2,1]
    bubble(mylist)
    print (mylist)


#problem 12
def no_short_strings1(mylist, n):
    newlist = []
    for i in range(len(mylist)):
        if len(mylist[i]) >= n:
            newlist += [mylist[i]]
    return newlist


#problem 13
def unique_chars(s):
    chars = []
    for i in range(len(s)):
        if s[i] in chars:
            return False
        chars = chars + [ s[i] ]
    return True


#problem 14
def unique_ints(mylist):
    uniques = []
    for i in range(len(mylist)):
        if mylist[i] not in uniques:
            uniques = uniques + [ mylist[i] ]
    return uniques


#problem 15
def translate_spaces(url):
    newurl = ''
    for i in range(len(url)):
        if url[i] == ' ':
            newurl += '%20'
        else:
            newurl += url[i]
    return newurl


#problem 16
def cmpOne(s1,s2):
    if len(s1) > len(s2):
        print (s1)
    else:
        print (s2)
    #won't work: s = cmpOne('alpha','beta') * 2

def cmpTwo(s1,s2):
    if len(s1) > len(s2):
        return s1
    else:
        return s2
    #will work: s = cmpTwo('alpha','beta') * 2


#problem 17
def cmpFirstLast(s):
    if s[0] < s[-1]:
        return True
    return False


#problem 18
def numBefore(s):
    count = 0
    for index in range(len(s)):
        if s[index] < 'h':
            count += 1
    return count

def numBefore(s):
    count = 0
    index = 0
    while index < len(s):
        if s[index] < 'h':
            count += 1
        index += 1
    return count
