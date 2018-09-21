
#  f(x)=3x^4-8x^3+6x^2-12 on [-3,3]

import numpy as np
import matplotlib.pyplot as plt

x=[-3,-2,-1,0,1,2,3]

def f(x):
    return 3*(np.power(x,4)) - 8*(np.power(x,3)) + 6*(np.power(x,2))-12

print (f(x))
plt.plot(x, f(x))
plt.show()
#just a comment to test git commit 2

a = 15


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))