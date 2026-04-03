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
