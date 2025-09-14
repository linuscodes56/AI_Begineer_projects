spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Inital spice mix: {spice_mix}")

spice_mix.add("lemon")
spice_mix.add("pudina")
print(f"Second spice mix id: {id(spice_mix)}") # id does not change, so mutable
print(f"Second spice mix: {spice_mix}")

