# lambda anonymous function
# x = lambda a: a + 10
# print(x(10))   # 10 + 10 = 20
# print(x(20))
# print(x(30))

# using lambda function with multiple arguments
# multiargs = lambda a, b, c : a + b + c
# print(multiargs(5, 10, 20))
# print(multiargs(30, 11, 4))

# return statement with lambda
def my_function(number):
    return lambda a : a * number

doubling = my_function(2)
tripling = my_function(3)

print(doubling(10))  # 10 * 2
print(tripling(20))  # 20 * 3
