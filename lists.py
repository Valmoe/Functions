def validate_entry():
    try:
        if int(a.element) >= 5:
            print(f"{int(a)}kg of maize is sustainable to the economy")
        else:
            print(f"We have {int(a)}kg, below thresh hold thus we need to restock our shelves")
    except ValueError:
        print("invalid entry")
a = " "
while a != "exit":
    a = input("Enter a value: ")
    for a.element in a.split(","):
        validate_entry()