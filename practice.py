#a = int(input("enter the number:"))
#if a > 0:
 #   print("positive")
#elif a < 0:
 #   print("negative")
#else:
#   print("zero")

#a = int(input("enter the first number:"))
#b = int(input("enter the second numbr:"))

#if b > a:
 #   print("b is greater")
#else:
#    print("a is greater")

#marks = int(input("enter the marks:"))

#f marks >= 90:
  #  print("A GRADE")
#elif marks >= 75:
 #   print("B GRADE")
#elif marks >= 50:
 #   print("C GRADE")
#else:
 #   print("FAIL")


#sum = 0
#for i in range(1, 11):
 #   sum = sum + i
#print(sum)




#for i in range(1, 11):
#    if i % 2 == 0:
#       print(i, "Even")
#   else:
#     print(i, "Odd")

#for i in range(1, 11):
 #   if i == 5: 
 # #print("FIVE")
#  else:
#       print(i)
#i =1
#while i <= 10:
#   print(i)
 #   i=i+1


#a = input("Enter the value: ")
#print(a)
#print(type(a))

#age=int(input("enter the age:"))
#if age > 18 :
 #   print("adult")
#else:
 #   print("minor")



#a= int(input("enter the number:"))
#if a >0:
#    print("positive")
#elif a < 0:
#    print("negative")
#else:
 #   print("zero")



#a=int(input("enter the first number:"))
#=int(input("enter the second number:"))
#if a > b:
#    print("a is greater")
#elif b > a :
#     print("b is greater")
#else:
#     print("both are equals")


#for i in range(1, 33):
 #   for j in range(1, i+1):
  #      print(j, end="")
   # print()

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# c=int(input("enter the third number:"))
# if a >= b and a >= c:
#     print("Largest is:", a)
# elif b >= a and b >= c:
#     print("Largest is:", b)
# else:
#     print("Largest is:", c)







# ch = input("Enter a character: ")

# if ch in "aeiouAEIOU":
#     print("Vowel")
# elif ch.isalpha():
#     print("Consonant")
# elif ch.isdigit():
#     print("Number")
# else:
#     print("Special Character")


# age = int(input("enter the age:"))

# if age <= 12:
#     print("Child.")
# elif age <= 19:
#     print("Teenager.")
# elif age <= 35:
#     print("Young adult.")
# else:
#     print("Adult.")
# import random
# words = ["APPLE", "MANGO", "BANANA", "ORANGE", "GRAPES"]
# word = random.choice(words)
# chances = 5
# print("Welcome to Hangman!")

# while chances > 0:
#     guess = input("Guess the word: ").upper()

#     if guess == word:
#         print( "You Win!")
#         break
#     else:
#         chances -= 1
#         print("Wrong Guess!")
#         print("Chances left:", chances)

# if chances == 0:
#     print("Game Over!")
#     print("The word was:", word)



# student = {
#     "name": (input("enter the  name:")),
#     "marks": [35,33,20]
# }

# total = sum(student["marks"])
# average = total / len(student["marks"])

# print("Name:", student["name"])
# print("Total Marks:", total)
# print("Average:", average)

# if average >=60:
#     print("Grade: A+")
# else:
#     print("Grade: B")





# name=input("enter the name:")
# marks = int(input("enter your marks(0-100):"))
# if marks < 0 or marks > 100:
#     print("Invlaid input! marks should be between 0 and 100.")
# elif marks >= 90:
#     print("grade: A+")
# elif marks >= 80:
#     print("grade: B+")
# elif marks >= 70:
#     print("grade: B")
# elif marks  >= 60:
#     print(("grade:C+"))
# elif marks >= 50:
#     print("grade:C")
# else:
#     print("failed")
print("Chatbot: Hi! I am a simple bot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hello there!")

    elif user == "hi":
        print("Chatbot: Hi! How can I help you?")

    elif user == "how are you":
        print("Chatbot: I'm fine, thanks! What about you?")

    elif user == "what is your name":
        print("Chatbot: I'm a Python chatbot.")

    elif user == "what can you do":
        print("Chatbot: I can answer simple questions using if-else logic.")

    elif user == "how is the weather":
        print("Chatbot: It's sunny today ")

    elif user == "what is python":
        print("Chatbot: Python is a popular programming language.")

    elif user == "who created you":
        print("Chatbot: I was created using Python code by a developer.")
    elif user == "what is ai":
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif user == "tell me a joke":
        print("Chatbot: Why did the computer go to the doctor? Because it had a virus 😂")

    elif user == "what is 2+2":
        print("Chatbot: 2 + 2 = 4")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day ")
        break

    else:
        print("Chatbot: Sorry, I don't understand that.")





















