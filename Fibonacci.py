def fib(valor):
    a = 0 
    b = 1
    while a < valor:
        print(a, end = ',')
        a, b = b, a+b
        

fib(700)