essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices # union
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices # intersection
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices # diff 
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}") # membership test

