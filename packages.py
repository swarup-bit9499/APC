def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

from MyPackage.addition import add
from MyPackage.multiplication import multiply

x = 10
y = 5

print("Addition =", add(x, y))
print("Multiplication =", multiply(x, y))