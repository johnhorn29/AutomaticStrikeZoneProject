# Use functions to print out the fibonacci numbers
# 1, 1, 2, 3, 5, 8, ...
def fc (f):
    celcius = (f-32)/(9/5)

    return celcius

print(fc(32))

def cf (c):
    farenheight = (9/5)*(c)+32

    return farenheight

print(cf(0))


def fib(seq):
    if seq == 1:
        return 1

    if seq == 2:
        return 1

    if seq >= 3:
        output = fib(seq-1) + fib(seq-2)
        return output

for i in range(30):
    print(fib(i+1))