# love_calculator
girl = input("enter girl's name")
boy = input("enter boy's name")
t = girl.count('t') + boy.count('t')
r = girl.count('r') + boy.count('r')
u = girl.count('u') + boy.count('u')
e = girl.count('e') + boy.count('e')
l = girl.count('l') + boy.count('l')
o = girl.count('o') + boy.count('o')
v = girl.count('v') + boy.count('v')
e = girl.count('e') + boy.count('e')
a = t+r+u+e
b = l+o+v+e
print(f"The love percentage between you two is {10*a + b} %")
