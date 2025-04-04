def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)
    

#Reemplazo por Lambda
def print_function1(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
 
print_function1([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)