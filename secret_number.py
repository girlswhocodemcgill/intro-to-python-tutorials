print("Please think of a number between 1 and 100")

upper_bound = 100 
lower_bound = 1  
correct = 0 
middle = int(( upper_bound + lower_bound ) / 2)

while c == 0: 
    print("Is your secret number", m, "?\n Enter 'h' if my guess is too high, 'l' if too low, or 'c' if I am correct: ")

    x = str(input())
    if x == "l":
        lower_bound = middle 
        middle = round(( upper_bound + lower_bound ) / 2)
        
    elif x == "h":
        upper_bound = middle 
        middle = int(( upper_bound + lower_bound ) / 2)
        
    elif x == "c":
        print("Your secret number was", middle)
        c = 1 
        
    else: 
       print("Unexpected input. Make sure you typed 'c', 'l', or 'h'.")
