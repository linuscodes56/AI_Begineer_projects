## Operators

# Chapter3: Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_falvour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strenght {powerful_falvour}")
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000 # for readablity
print(f"tea leaves: {total_tea_leaves_harvested}")

# chapter 4: bool 
is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting/ type casting implicit
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk, eg: [], (), False, None, ""
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")

# Chapter5: Real/float
import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }") # 0.010000000000005116 when current_temp = 95.49
print(sys.float_info)