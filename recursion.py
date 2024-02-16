from sys import getrecursionlimit
x= getrecursionlimit()
print(x)

from sys import setrecursionlimit
setrecursionlimit(2000)
x= getrecursionlimit()
print(x)

def function():
    x = 10
    function()

function()
