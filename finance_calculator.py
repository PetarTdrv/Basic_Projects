principal_amount = float(input("Enter principal amount: "))
annual_interest = float(input("Enter annual interest rate: "))
period = int(input("Enter investment period in years: "))

addition = 0

addition_option = input("Do you want to add additions? (yes/no): ").lower()

if addition_option == "yes":
    number_of_additions = int(input("Enter the number of additions: "))

    for _ in range(number_of_additions):
        new_addition = float(input("Enter the amount of addition: "))
        addition += new_addition
elif addition_option == "no":
    print("No additions.")

principal_amount += addition

percent_in_float = annual_interest / 100

period_in_months = period * 12 

final_capital = principal_amount * (1 + percent_in_float/12)**(period_in_months + number_of_additions)

print(f"The final capital after {period} years is: {final_capital:.2f}")
