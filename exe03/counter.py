def counter():
    x = 0
    def internal():
        nonlocal x
        x += 1
        return x
    return internal

count = counter()

print(count())
print(count())
print(count())
print(count())
print(count())
print(count())