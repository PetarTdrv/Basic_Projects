years = int(input("Enter years: "))
months = years * 12
days_in_year = 365.242199
days = days_in_year * years

print(f"Years - {years} -> Months - {months} -> Days - {days:.0f}")