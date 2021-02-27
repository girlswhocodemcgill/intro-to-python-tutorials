a = int(input("Please enter an input: "))

def prime(a):
    if(a == 1 or a == 2): 
        print("It is a prime number.")
    
    for x in range(2, a):
        if (a % x == 0):
            print("It is not a prime number.")
    
    print("It is a prime number.")

prime(a)