masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices # we need to know know how many numbers are we extracting

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1 # behind the scene this is tuple
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio # swap two numbers
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# membership testing
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")