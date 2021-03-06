def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
      yield b
      a, b = b, a+b
      n=n+1
    return 'done'
    
f=fib(10)
print('fib(10):',f)
for x in f:
    print(x)
    
# call generator manually:
g=fib(5)
while 1:
    try:
        x=g.send(None)
        print('g:',x)
    except StopIteration as e:
      print('Generator return value:', e.value)
      break
#call generator using iter:
i=iter(fib(5))
while 1:
    try:
        r=next(i)
        print('i:',r)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
