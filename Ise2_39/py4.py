color_tuple = ("red", "green", "blue", "yellow", "purple", "orange")
user_color = input("Enter a color to check: ").strip().lower()
if user_color in color_tuple:
    print(f"Yes! '{user_color}' exists in the color tuple.")
else:
    print(f"No, '{user_color}' does not exist in the color tuple.")
