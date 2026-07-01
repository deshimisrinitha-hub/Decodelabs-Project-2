THRESHOLD = 30

while True:
    moisture = int(input("Enter soil moisture percentage (0-100): "))

    if moisture < THRESHOLD:
        print("Soil is Dry")
        print("Pump ON")
    else:
        print("Soil is Wet")
        print("Pump OFF")

    print("-" * 30)