# # Print Your Name & Age

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))


print("Hello",name + "!", "You are", age, "years old")


# # Practice 2: Simple Calculator
firstNumber = int(input("Enter First Number: "))
secondNumber = int(input("Enter Your Second Number"))

sumation = firstNumber + secondNumber
div = firstNumber - secondNumber
product = firstNumber * secondNumber
Quotient = firstNumber / secondNumber

print("Sum:", sumation)
print("Difference:", div)
print("Product:", product)
print("Quotient:", Quotient)

# # Practice 3: Even or Odd

number = int(input("Enter a Number: "))

if (number % 2) == 0:
    print (number, "is an even number")
else:
    print(number, "is an odd number")

#  Practice 4: Guess the Secret Number

import random  # Import the random module

# # Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print(secret_number)

# # Ask the user to guess
while True:
    guess = int(input("Guess the number (1-10): "))  # Take input from the user

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it! 🎉")
        break  # Exit the loop when the guess is correct


# 📝 Practice 5: Multiplication Table
