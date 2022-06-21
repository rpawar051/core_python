## generate fibonacci number upto n

def fib(n):

    p, q = 0, 1
    # yield n*2
    while(p<n):
        yield p
        p, q = q, p + q

# create a generator objects
x = fib(10)
print(x)
# iterating using __next__() for python2  use next()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())






# for i in fib(10):
#     print(i)