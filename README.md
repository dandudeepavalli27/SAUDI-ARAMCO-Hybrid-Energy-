# SAUDI-ARAMCO-Hybrid-Energy
Aim
To implement a rule-based energy management system for switching to charging mode.
General Objective
To understand hybrid energy management systems and how threshold-based decisions ensure continuous operation of autonomous robots.
Specific Objective
To apply the rule:
Battery Level = 18%
Threshold = 20%
If battery < threshold → Switch to Charging Mode
Dataset
Battery Health Dataset
Source: Kaggle
Procedure
Input battery level
Define threshold value
Compare battery with threshold
If battery < threshold → Charging mode
Display result
Algorithm
Start
Input battery level
Set threshold
If battery < threshold → Charging Mode
Else → Normal Operation
Display result
Stop
Code Logic
if battery < threshold:
    mode = "Charging Mode"
Python Code
# SESSION 29 – Hybrid Energy Management

# Step 1: Input values
battery = 18   # battery percentage
threshold = 20 # critical level

# Step 2: Apply rule
if battery < threshold:
    print("Switch to Charging Mode")
else:
    print("Continue Operation")

print("\nProgram Executed Successfully")
Output
Switch to Charging Mode

Program Executed Successfully
Result
Since the battery level is below threshold:
Charging Mode is activated
Industry Application
Energy management is used in:
Industrial robots
Autonomous systems
Electric vehicles
Smart grids
Companies like Saudi Aramco use this in:
Industrial automation
Energy optimization
Smart monitoring systems
Conclusion
Threshold-based energy management ensures continuous operation and prevents system failure by triggering timely recharging.
