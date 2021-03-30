def maxNElement(list, n):
    res = []

    for i in range(0, n):
        max = 0
        for j in range(len(list)):
            if list[j] > max:
                max1 = list[j];

        list.remove(max);
        res.append(max)

    print(res)


# Driver code
list = [2, 6, 41, 85, 0, 3, 7, 6, 10]
n = 2

# Calling the function
maxNElement(list, n)