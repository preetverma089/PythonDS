# ye h mutable datatypes examples
# set ek datatype h python me jst like other
# ye mutable h isme values changes hoti h 
# integers me nya refrence bnta h 
# integers ke brre me or revised k lie chapter 3 h 
spice_Mix = set()
print(f"Initial SpiceMix id: {spice_Mix}")
print(f"Initial SpiceMix id: {id(spice_Mix)}")

spice_Mix.add("Ginger")
spice_Mix.add("cardamom")
print(f"after SpiceMix id: {id(spice_Mix)}")
print(f"after SpiceMix id: {spice_Mix}")