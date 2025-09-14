# Chapter 8
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")


# Chapter 9
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}") # Normally + is for numbers, but here it works for combining lists.

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

# Converting String → List-like Object. bytearray represents a mutable sequence of integers (0–255).
# Each character of the string is represented as bytes.

# Methods on bytearray
# Behaves like a mutable list.
# Supports methods like append(), replace(), etc.

# why use this bytearray? as string is immutable and we want mutable object within string
# Rarely used in normal Python string/list handling, but useful for low-level operations like data manipulation or binary encoding.

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")