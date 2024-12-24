import random

num = random.randrange(10, 100)
print("The random number is:", num)

lives =int(input("How many lives you want : "))

while lives > 0:
    ans = int(input("Please enter a number: "))
    
    if ans > num:
        print("Too large")
    elif ans < num:
        print("Too small")
    else:
        print("Congratulations! You guessed the number correctly:", num)
        break
    
    lives -= 1  # Decrement the number of lives after each guess
    print("You have", lives, "lives left.")
else:
    print("Out of lives! The number was:", num)
