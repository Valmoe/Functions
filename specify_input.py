a = input("Enter a value: ")

def validate_entry():
    if a.isdigit():
        if int(a) >= 5:
            print(f"{int(a)}kg of maize is sustainable to the economy")
        else:
            print(f"We have {int(a)}kg, below thresh hold thus we need to restock our shelves")
    else:
        print("invalid entry")
validate_entry()