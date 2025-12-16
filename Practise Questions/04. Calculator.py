def calc(a, b, op):
    if op == '+':
        print(f"{a} {op} {b} = {a + b}")
        return a + b
    if op == '-':
        print(f"{a}{op}{b} = {a-b}")
        return a - b
    if op =='/':
        print(f"{a}{op}{b} = {a/b}")
        return a/b
    if op == '%':
        print(f"{a}{op}{b} = {a%b}")
        return a%b
    if op == '*':
        print(f"{a}{op}{b} = {a*b}")
        return a*b

a = float(input('What is the first number?: ') )

while True:
    op = input('+\n-\n*\n/\nPick an operation: ')
    b = float(input("Whats the next number?: "))
    ans = calc(a, b, op)
    print('The answer is', str(ans))
    ch = input('. Enter "yes" to continue with the result or enter "no" to start over. Enter anything else to exit'.lower())
    if ch == 'yes':
        a= ans
        continue
    elif ch == 'no':
        a = float(input('What is the first number'))
        continue
    else:
        break

#Other methods may include:
# def add(a,b)
#     return a+b
# def sub(a,b)
#     return a - b
#
# operations = {
#     '+' : add,
#     '-' : sub,
#     '*' : mul,
#     '/' : div,
#     '%' : rem,
# }
# print(operations['+'](3,4))



