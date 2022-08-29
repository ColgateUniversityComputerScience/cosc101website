def foo(y):
    if y < 10:
        return y
    srt = str(y)[-1]
    end = str( str(y)[:-1] )
    end_r = str( foo( int(end) ) )
    return int( srt + end_r )

print( foo(0) )
print( foo(10) )
print( foo(143) )
print( foo(6543) )
print( foo(5030) )
