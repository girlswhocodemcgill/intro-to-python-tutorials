a = int(input("Please enter a number: "))

result = 0

for i in range(1, a):
    if (a % i == 0):
        result += i

print(result == a)