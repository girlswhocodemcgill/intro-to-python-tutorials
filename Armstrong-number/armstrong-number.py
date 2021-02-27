number = input("Enter a number: ")
digit_nums = len(number) # inputs are strings!
number = int(number)
tmp = number
sum = 0

while(tmp > 0):
    last_digit = tmp % 10
    sum += last_digit ** digit_nums
    tmp = tmp // 10 


if(number == sum):
    print("Yes!")
else:
    print("No!")
