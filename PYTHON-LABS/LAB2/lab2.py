##1
# def increased(length=0, start=0):
#     les = []
#     for i in range(start, start + length):
#         les.append(i)
#     return les

# print(increased(5, 3))

#2
# def divided(num=0):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
    
# print(divided(9))
# print(divided(10))
# print(divided(15))
# print(divided(7))

#3
# def stringinput(text=""):
#    if text.isdigit():
#         return "Error: Input must be a string"
#    return text[::-1]

# str_input = input("Enter string: ")
# print(stringinput(str_input))

#4
# username = input("Enter your username: ")
# if not username or username.isdigit():
#     print("Error: Please enter a valid name (letters only).")
# else:
#     email = input("Enter your email: ")
#     if "@" in email and "." in email:
#         print(f"user date is 1-name:{username} 2-email:{email}")
#     else:
#         print("Error: Invalid email.")

#5
# def string(text):
#       longest = text[0]
#       current = text[0]
#       for i in range(1 , len(text)):
#             if  text[i] >= text[i-1]:
#                   current += text[i]
#             else:
#                   if len(current) > len(longest):
#                         longest = current
#                   current = text[i]

#       return longest

# print(string("abdulrahman"))

#6 
# inputuser = ""
# numbers = []
# while inputuser != "done":
#     inputuser = input("enter number: ")

#     if inputuser == "done":
#         break  
#     elif inputuser.isdigit():
#         numbers.append(int(inputuser))
# total = sum(numbers)
# count = len(numbers)
# average = total / count
# print (numbers)
# print(total)
# print(count)
# print(average)
 
#7
import random

words = ["apple", "banana", "orange", "grapes"]

word = random.choice(words)

name = input("Enter your name: ")

guessed_letters = []
turns = 7

while turns > 0:
    output = ""
    for c in word:
        if c in guessed_letters:
            output += c
        else:
            output += "."

    print(output)

    if "." not in output:
        print("bravo")
        break

    guess = input("guess a letter: ")

    if guess not in word:
        turns -= 1
        print(f"wrong You have {turns} turns left")
    else:
        guessed_letters.append(guess)

if turns == 0:
    print(f"game ove")