#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == "ADMIN" or "admin" and password == "12345":
        return(print("Accsess granted"))
    else:
        print("Access denied")
# #tests
# admin_login("johnn", "2")
# admin_login("ADMIN", "12345")
# admin_login("admin", "12345")


def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return(print("It's brisk out there!"))
    elif 40 <= temperature <= 65:
        return(print("It's a little chilly out there!"))
    elif temperature > 85:
        return(print("It's too dang hot out there!"))
    else:
        return(print("It's perfect out there!"))
# #tests
# hows_the_weather(12)
# hows_the_weather(40)
# hows_the_weather(50)
# hows_the_weather(65)
# hows_the_weather(76)
# hows_the_weather(85)
# hows_the_weather(90)

def fizzbuzz(num):
    # your code here
    if num % 3 and num % 5 == 0:
        return(print("FizzBuzz"))
    elif  num % 3 == 0:
        return(print("Fizz"))
    elif num % 5 == 0:
        return(print("Buzz"))
    else:
        return(print(num))
# #tests
# fizzbuzz(3)
# fizzbuzz(6)
# fizzbuzz(5)
# fizzbuzz(15)
# fizzbuzz(10)
# fizzbuzz(20)
# fizzbuzz(1)
# fizzbuzz(2)



def calculator(operation, num1, num2):
    # Using if/elif
    # if operation == "+":
    #     return(print(num1 + num2))
    # elif operation == "-":
    #     return(print(num1 - num2))
    # elif operation == "*":
    #     return(print(num1 * num2))
    # elif operation == "/":
    #     return(print(num1 / num2))
    # else:
    #     print("Invalid Operation!")
    #     return None

    #Using dictionary mapping
    num_map = {
        "+" : num1 + num2,
        "-" : num1 - num2,
        "*" : num1 * num2,
        "/" : num1 / num2,
    }
    ops = num_map.get(operation, "Invalid operation!")
    print(ops)

#tests
calculator("+", 2,3)
calculator("-", 2,3)
calculator("/", 2,3)
calculator("*", 2,3)
calculator("//", 2,3)