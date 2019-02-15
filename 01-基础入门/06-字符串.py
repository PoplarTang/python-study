str = "Hello world!"

print(str[:5])
print(str[6:])
print(str[::-1])
print(str[1:5])
print(str[-6:-1])
print(str[-2:-7:-1])

str = "hello"

print(str.ljust(10, "="))

str = str.center(30, "-")
print(str)

str = str.lstrip('-')
print(str)
