# Read the day
print("Enter day (1-8): ", end="")
day = int(input())

# Initialize counters
children = 0
adults = 0
seniors = 0

# Read ages until -1
while True:
    print("Enter age (-1 to stop): ", end="")
    age = int(input())
    if age == -1:
        break
    if age <= 12:
        children += 1
    elif age >= 60:
        seniors += 1
    else:
        adults += 1

# Determine day type and prices
if day <= 5:
    day_type = "weekday"
    child_price = 30
    adult_price = 60
    senior_price = 40
    group_price = 35
elif day <= 7:
    day_type = "weekend"
    child_price = 40
    adult_price = 80
    senior_price = 50
    group_price = 65
else:
    day_type = "holiday"
    child_price = 50
    adult_price = 100
    senior_price = 60
    group_price = 75

# Compute groups
groups_formed = adults // 5
leftover_adults = adults % 5

# Compute cost
cost = children * child_price + seniors * senior_price + groups_formed * 5 * group_price + leftover_adults * adult_price

# Compute discount
if (day_type == "weekend" or day_type == "holiday") and groups_formed > 0:
    discount = 0.1 * cost
else:
    discount = 0.0

# Compute service fee
total_people = children + adults + seniors
if day_type == "weekday" and total_people < 3:
    service_fee = 0
else:
    service_fee = 5 * total_people if 5 * total_people <= 30 else 30

# Compute total cost
total_cost = cost - discount + service_fee

# Output
print("Day type:", day_type)
print("Children:", children)
print("Adults:", adults)
print("Seniors:", seniors)
print("Total people:", total_people)
print("Groups formed:", groups_formed)
print("Discount:", "{:.2f}".format(discount))
print("Service fee:", "{:.2f}".format(service_fee))
print("Total cost:", "{:.2f}".format(total_cost))
