# ==========================================================
# OHM'S LAW & POWER CALCULATOR
# This program calculates Voltage, Current, Resistance,
# or Power based on the user's choice.
# ==========================================================

# Display the welcome message
print("=" * 60)
print("WELCOME TO OHM'S LAW & POWER CALCULATOR")
print("=" * 60)

# Display the list of calculations available
print("\nSelect what you want to calculate:")
print("1. Voltage (V)")
print("2. Current (I)")
print("3. Resistance (R)")
print("4. Power (P)")

# Ask the user to enter their choice
choice = input("Enter your choice (1-4): ")

# If the user wants to calculate Voltage
if choice == "1":

    # Ask the user to enter the current value
    current = float(input("Enter Current (A): "))

    # Ask the user to enter the resistance value
    resistance = float(input("Enter Resistance (Ω): "))

    # Calculate voltage using Ohm's Law
    voltage = current * resistance

    # Display the result
    print(f"Voltage = {voltage} Volts")

# If the user wants to calculate Current
elif choice == "2":

    # Ask the user to enter the voltage value
    voltage = float(input("Enter Voltage (V): "))

    # Ask the user to enter the resistance value
    resistance = float(input("Enter Resistance (Ω): "))

    # Calculate current
    current = voltage / resistance

    # Display the answer
    print(f"Current = {current} Amperes")

# If the user wants to calculate Resistance
elif choice == "3":

    # Ask the user to enter the voltage value
    voltage = float(input("Enter Voltage (V): "))

    # Ask the user to enter the current value
    current = float(input("Enter Current (A): "))

    # Calculate resistance
    resistance = voltage / current

    # Display the answer
    print(f"Resistance = {resistance} Ohms")

# If the user wants to calculate Power
elif choice == "4":

    # Display the available power formulas
    print("\nChoose a Power Formula")
    print("1. P = V × I")
    print("2. P = I² × R")
    print("3. P = V² ÷ R")

    # Ask the user which formula to use
    formula = input("Enter your choice (1-3): ")

    # Calculate power using V × I
    if formula == "1":

        # Get voltage from the user
        voltage = float(input("Enter Voltage (V): "))

        # Get current from the user
        current = float(input("Enter Current (A): "))

        # Calculate power
        power = voltage * current

        # Display the result
        print(f"Power = {power} Watts")

    # Calculate power using I²R
    elif formula == "2":

        # Get current value
        current = float(input("Enter Current (A): "))

        # Get resistance value
        resistance = float(input("Enter Resistance (Ω): "))

        # Calculate power
        power = (current ** 2) * resistance

        # Display the result
        print(f"Power = {power} Watts")

    # Calculate power using V²/R
    elif formula == "3":

        # Get voltage value
        voltage = float(input("Enter Voltage (V): "))

        # Get resistance value
        resistance = float(input("Enter Resistance (Ω): "))

        # Calculate power
        power = (voltage ** 2) / resistance

        # Display the result
        print(f"Power = {power} Watts")

    # Display an error if an invalid formula is selected
    else:
        print("Invalid Power Formula.")

# Display an error if the user enters an invalid menu choice
else:
    print("Invalid Menu Choice.")


print("=" * 60)
print("THANKS FOR CHOOSING OHM'S LAW CALCULATOR")
print("=" * 60)
