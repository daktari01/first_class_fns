def square(x):
    return x* x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    #result = [result.append(func(i) for i in arg_list)]
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

