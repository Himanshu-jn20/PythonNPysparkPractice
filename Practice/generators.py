def fib_gen():
    a, b = 0, 1
    while True:
        #print(a)
        yield a
        a, b = b, a+b

fibo=fib_gen() # generator obj created , simply iterators
print(type(fibo))

print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))

for f in fibo:
    if f>100:
        break

