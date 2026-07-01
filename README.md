Decodelabs 
Project 2: Automated Irrigation Controller (Software Simulation)

Overview

This project simulates an Automated Irrigation Controller using Python. The system monitors soil moisture levels and automatically controls a water pump based on predefined threshold values. Since this is a software simulation, user input is used to represent soil moisture sensor readings.

Objective

To design a closed-loop irrigation system that:

- Reads soil moisture values.
- Evaluates the moisture level against a threshold.
- Turns the water pump ON when the soil is dry.
- Turns the water pump OFF when the soil is sufficiently moist.

Tools Used

- Visual Studio Code (VS Code)
- Python 3.x

Project Logic

1. The user enters a soil moisture percentage value (0–100).
2. The program compares the value with a threshold of 30%.
3. If the moisture value is below 30%, the soil is considered dry and the pump is turned ON.
4. If the moisture value is 30% or higher, the soil is considered wet and the pump is turned OFF.

Python Code

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

Sample Output

Case 1: Dry Soil

Enter soil moisture percentage (0-100): 20
Soil is Dry
Pump ON

Case 2: Wet Soil

Enter soil moisture percentage (0-100): 75
Soil is Wet
Pump OFF

Applications

- Smart Agriculture
- Automated Irrigation Systems
- Water Conservation Projects
- IoT-based Farming Solutions

Conclusion

The project successfully demonstrates the working principle of an Automated Irrigation Controller through software simulation. The system uses threshold-based decision making to control irrigation automatically, reducing manual intervention and improving water management efficiency.

Author

Srinitha Deshimi
