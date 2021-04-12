weight = input("Weight: ")
choice = input("Do you wish to convert to lbs(L) or  kg(K)? ")
if choice=='K':
    converted_weight = float(weight)*0.4535
    print("Weight in kilograms: ",converted_weight)
elif choice=='L':
    converted_weight = float(weight) * 2.2046
    print("Weight in pounds: ", converted_weight)
else:
    print("Wrong choice.")