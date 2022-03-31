# 1.0

print("Electricity bill estimator")
cents_per_kWh = float(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))

bill = cents_per_kWh * days * daily_use * 0.01

print(f"Estimated bill: ${bill:.2f}")


# 2.0

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff = float(input("Which tariff? 11 or 31: "))

while tariff not in [11, 31]:
    print("Invalid value")
    tariff = float(input("Which tariff? 11 or 31: "))

daily_use = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days: "))

if tariff == 11:
    bill = TARIFF_11 * days * daily_use
    print(f"Estimated bill: ${bill:.2f}")

elif tariff == 31:
    bill = TARIFF_31 * days * daily_use
    print(f"Estimated bill: ${bill:.2f}")
