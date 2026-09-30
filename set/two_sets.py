# 19.	Create two sets:
# Students present in the morning session ,Students present in the afternoon session 
# Find:Students present in both sessions ,Students present only in the morning ,Students present only in the afternoon ,Students present in at least one session
set1 = {"Srushhti","Arya","Aditi","Rahul","Harsh"}
set2 = {"Arya","Vaishnavi","Aditi","siddhi","vedika"}
print("Present in both:", set1 & set2)
print("Only morning:", set1 - set2)
print("Only afternoon:", set1 - set2)
print("At least one session:", set1 | set2)