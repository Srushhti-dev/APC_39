tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

unique = ()

for n in merged:
    if n not in unique:
        unique = unique + (n,)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Merged tuple:", merged)
print("After removing duplicates:", unique)