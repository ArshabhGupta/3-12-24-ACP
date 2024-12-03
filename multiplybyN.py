m = int(input("Enter a value: "))
n = int(input("Enter a value: "))
num = int(input("Enter the number of time you want to multiply: "))

def function(m, n):
    a = m * n
    return a
print(function(m, n))

def function(m, n, num):
    for i in range(1, num + 1):
        m = m * n
    return m
print(function(m, n, num))