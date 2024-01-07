import random

# Bank Account
country = input("Enter place of card('bg', 'de', 'fr', 'it', 'gb'): ").lower() 
owner = input("Enter your name: ")
balance = float(input("Enter start balance: "))
type_of_currency = input("Enter currency of card('BGN', 'USD', 'EUR'): ").lower() # "BGN", "USD", "EUR"

random1 = random.randint(1, 9)
random2 = random.randint(1, 9)
random3 = random.randint(1, 9)
random4 = random.randint(1, 9)

pin = 5376
pin = (f"{random1}{random2}{random3}{random4}")
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

print(f"\nOwner of card is: {owner}")
print(f"Iban of card is: {iban}")
print(f"PIN of card is: {pin}")

while True:
    conf = input("\nWhat operation do you want to do?(deposit/withdrawal/reference)").lower()

    if conf == "reference":
        pin_identification = input("Enter your pin: ")
        if pin_identification == pin:
            print(f"\nOwner: {owner}")
            print(f"IBAN: {iban}")
            print(f"Balance: {balance:.2f}")
            break
    elif conf == "deposit":
        pin_identification = input("\nEnter your pin: ")
        if pin_identification == pin:
            tp_vl = input("Enter the currency you will deposit('BGN', 'USD', 'EUR'): ").lower()
            deposit = float(input("Enter the amount you will deposit: "))
            if deposit < 0:
                print("Invalid operation!")
            elif type_of_currency == "bgn":
                if tp_vl == "bgn":
                        balance += deposit
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif tp_vl == "usd":
                        changed_value = deposit * 1.78
                        balance += changed_value
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif tp_vl == "eur":
                        changed_value = deposit * 1.96
                        balance += changed_value
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif type_of_currency == "usd":
                    if tp_vl == "usd":
                        balance += deposit
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif tp_vl == "bgn":
                        changed_value = deposit * 0.56
                        balance += deposit
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif tp_vl == "eur":
                        changed_value = deposit * 1.10
                        balance += deposit
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif type_of_currency == "eur":
                    if tp_vl == "eur":
                        balance += deposit
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif tp_vl == "bgn":
                        changed_value = deposit * 0.51
                        balance += changed_value
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                elif tp_vl == "usd":
                        changed_value = deposit * 0.91
                        balance += changed_value
                        conf = input("Would you like a reference(yes/no): ")
                        if conf == "yes":
                            print(f"\nOwner: {owner}")
                            print(f"IBAN: {iban}")
                            print(f"Balance: {balance:.2f}")
                            break
                        elif conf == "no":
                            break
                break
    elif conf == "withdrawal":
        pin_identification = input("\nEnter your pin: ")
        if pin_identification == pin:
            withd = float(input("Enter the withdrawal amount: "))
            balance -= withd
            conf = input("Would you like a reference(yes/no): ")
            if conf == "yes":
                print(f"\nOwner: {owner}")
                print(f"IBAN: {iban}")
                print(f"Balance: {balance:.2f}")
                break
            elif conf == "no":
                break
