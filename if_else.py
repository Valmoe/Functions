user_input = input("Enter any number to verify if it is an even number: ")

def condition():
    if int(user_input)%2 == 0:
        return ("The number is even")
    else:
        return ("The number is odd")

user_output = condition()
print(user_output)