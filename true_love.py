# Love Calculator

girl = input("Enter girl's name: ").lower()
boy = input("Enter boy's name: ").lower()

# Count letters in "TRUE"
t = girl.count('t') + boy.count('t')
r = girl.count('r') + boy.count('r')
u = girl.count('u') + boy.count('u')
e = girl.count('e') + boy.count('e')

# Count letters in "LOVE"
l = girl.count('l') + boy.count('l')
o = girl.count('o') + boy.count('o')
v = girl.count('v') + boy.count('v')
e2 = girl.count('e') + boy.count('e')  # Count 'e' again for LOVE

# Calculate scores
a = t + r + u + e
b = l + o + v + e2

# Final percentage
love_percentage = int(str(a) + str(b))

print(f"The love percentage between you two is {love_percentage}%")
