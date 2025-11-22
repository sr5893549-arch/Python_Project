import random

# All characters we can use
a = "abcdefghijklmnopqrstuvwxyz"
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "0123456789"
s = "!@#$%^&*"

all = a + A + n + s

# Main loop
while True:
    print("\nPassword Tool")
    print("1. Make password")
    print("2. Check password")
    print("3. Exit")
    
    c = input("Choose 1-3: ")
    
    if c == "1":
        pwd = ""
        pwd += random.choice(a)
        pwd += random.choice(A) 
        pwd += random.choice(n)
        pwd += random.choice(s)
        
        for i in range(8):
            pwd += random.choice(all)
            
        pwd = ''.join(random.sample(pwd, len(pwd)))  # shuffle
        print("Your password:", pwd)
        
    elif c == "2":
        p = input("Your password: ")
        score = 0
        if len(p) >= 8:   score += 1
        if len(p) >= 12:  score += 1
        if any(x in a for x in p): score += 1
        if any(x in A for x in p): score += 1
        if any(x in n for x in p): score += 1
        if any(x in s for x in p): score += 1
        
        if score >= 5:   print("Strong")
        elif score >= 4: print("Good")
        else:            print("Weak")
            
    elif c == "3":
        print("Bye!")
        break