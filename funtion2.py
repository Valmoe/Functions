rent = 600
shopping = 15000
savings = 5000

def monthly_expense(months, message):
    print(f"In {months} months, Valentine Gumo spends {rent*months} on rent, {shopping*months} on shopping and lastly {savings*months} retains as savings")
    print(message)
monthly_expense(1,"First month")
monthly_expense(12, "a year")
monthly_expense(100,"sampled number")

