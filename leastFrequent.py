test_str = "GirlsWhoCode"

# printing original string
print("The original string is : " + test_str)

# using naive method to get least frequent character in string
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)

# printing result
print("The minimum of all characters in " + test_str + " is : " + str(res))