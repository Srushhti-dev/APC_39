dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"x": 20, "y": 40, "z": 30}
common = set(dict1.values()) & set(dict2.values())
print("Common values:", common)
