# Bank Account
country = input("Enter place of card: ").lower() 
owner = input("Enter your name: ")
balance = float(input("Enter balance: "))
type_of_currency = input("Enter currency of card('BGN', 'USD', 'EUR'): ") # "BGN", "USD", "EUR"

pin = 5376
iban = ""
print("\nYour account was created!")

if country == "bg":
    iban = "BG80BNBG96611020345678"
elif country == "de":
    iban = "DE89123456789012345678"
elif country == "fr":
    iban = "FR5312345678901234567890123"
elif country == "it":
    iban = "IT97X1234567890123456789012"
elif country == "gb":
    iban = "GB36675960161331926819"
else:
    iban = "EU456234293452304290867"

print(f"Owner of card is: {owner}")
print(f"Iban of card is: {iban}")
print(f"PIN of card is: {pin}")

while True:
    check = input("Would you like to make a reference(yes/no): ").lower()
    if check == "yes":
        validation = input("Enter your iban: ")
        if validation == iban:
            print("You have successfully logged in system!")
            print(f"Owner: {owner}")
            print(f"Balance: {balance:.2f}{type_of_currency}")
            break

    condition = input("\nWould you like to make a deposit(yes/no): ").lower()
    if condition == "yes":
        tp_vl = ("Enter currency type: ").lower()
        deposit = float(input("Enter sum for deposit: "))
        if type_of_currency == "bgn":
            if tp_vl == "bgn":
                balance += deposit
            elif tp_vl == "usd":
                changed_value = deposit * 1.78
                balance += changed_value
            elif tp_vl == "eur":
                changed_value = deposit * 1.96
                balance += changed_value
        elif type_of_currency == "usd":
            if tp_vl == "usd":
                balance += deposit
            elif tp_vl == "bgn":
                changed_value = deposit * 0.56
                balance += deposit
            elif tp_vl == "eur":
                changed_value = deposit * 1.10
                balance += deposit
        elif type_of_currency == "eur":
            if tp_vl == "eur":
                balance += deposit
            elif tp_vl == "bgn":
                changed_value = deposit * 0.51
                balance += changed_value
            elif tp_vl == "usd":
                changed_value = deposit * 0.91
                balance += changed_value
    elif condition == "no":
        defs = input("Do you want to make a withdrawal(yes/no): ").lower()
        if defs == "yes":
            withdrawal = float(input("Enter sum for withdrawal: "))
        elif defs == "no":
            break
        break
