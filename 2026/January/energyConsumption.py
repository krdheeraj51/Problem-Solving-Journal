# Energy Consumption
# Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.

# To compare them, convert both values to joules using the following conversions:

# 1 Calorie equals 4184 joules.
# 1 watt-hour equals 3600 joules.
# Return:

# "Workout" if the workout used more energy.
# "Devices" if the device used more energy.
# "Equal" if both used the same amount of energy.

def energy_consumption(calories_burned, watt_hours_used):
    calories_joules = calories_burned * 4184
    watt_hours_joules = watt_hours_used * 3600
    
    if calories_joules > watt_hours_joules:
        return "Workout"
    elif watt_hours_joules > calories_joules:
        return "Devices"
    else:
        return "Equal"
# Example usage:
calories_burned = 100   
watt_hours_used = 120  
print(energy_consumption(calories_burned, watt_hours_used))  # Output: "Workout"
