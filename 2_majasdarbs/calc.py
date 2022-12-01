#!/usr/bin/env python3

def summa(a, b):
    return a+b
    
def atnemsana(a, b):
    return a-b

def multiplikacija(a, b):
    return a*b

def dalisana(a, b):
    if b == 0:
        exit()
    else:
        return a/b

def eksponenta(a, b):
    return a**b

def check_float(x):
    if not x.replace('.', '', 1).isdigit():
        exit() 
    else:
        return float(x)

if __name__ == "__main__":
    assert summa(1,2) == 3
    assert atnemsana(3,1) == 2
    assert multiplikacija(1,2) == 2
    assert dalisana(2,2) == 1
    assert eksponenta(2,2) == 4