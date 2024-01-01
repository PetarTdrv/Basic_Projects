type_of_value = input() #Enter USD; GBP; EUR
money_you_have = float(input())# Enter your money
to_convert_money = input()#Enter money to covert USD; GBP; EUR
 
#USD
usd_to_GBP = 0.78544
usd_to_EUR = 0.91105
 
#GBP
gbp_to_USD = 1.274161
gbp_to_EUR = 1.162168
 
#EUR
eur_to_USD = 1.094369
eur_to_GBP = 0.86069
 
if type_of_value == "USD":
    if to_convert_money == "GBP":
        converted_money = money_you_have * usd_to_GBP
        print(f"{converted_money:.2f}")
    elif to_convert_money == "EUR":
        converted_money = money_you_have * usd_to_EUR
        print(f"{converted_money:.2f}")
elif type_of_value == "GBP":
    if to_convert_money == "USD":
        converted_money = money_you_have * gbp_to_USD
        print(f"{converted_money:.2f}")
    elif to_convert_money == "EUR":
        converted_money = money_you_have * gbp_to_EUR
        print(f"{converted_money:.2f}")
elif type_of_value == "EUR":
    if to_convert_money == "USD":
        converted_money = money_you_have * eur_to_USD
        print(f"{converted_money:.2f}")
    elif to_convert_money == "GBP":
        converted_money = money_you_have * eur_to_GBP
        print(f"{converted_money:.2f}")
elif type_of_value != "USD" and type_of_value != "GBP" and type_of_value != "EUR":
    if to_convert_money != "USD" and to_convert_money != "GBP" and to_convert_money != "EUR":
        print("There is no such currency in this converter.")
