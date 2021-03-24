def num(limit):
sum = 0
for i in range(0,limit+1):
if i%3==0 or i%5==0:
sum +=i
print(sum)
