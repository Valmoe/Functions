def validate_entry():
    try:
        entered_number= int(entered_number_element)
        if entered_number >= 5:
            print(f"{input_number}kg of maize is sustainable to the economy")
        elif entered_number < 5:
            print(f"We have {input_number}kg, below thresh hold thus we need to restock our shelves")
        else:
            print("You entered zero!")
    except ValueError:
        print("invalid entry")


input_number = ""
while input_number != "exit":
    input_number = input("Enter a number: ")
    print(type(input_number.split()))
    print(input_number.split())
    print(set(input_number.split()))
    for entered_number_element in set(input_number.split()):
        validate_entry()
