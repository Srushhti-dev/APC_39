# 25.	Represent the friends of two users using sets. Find:
# •	Mutual friends 
# •	Friends unique to User 1 
# •	Friends unique to User 2 
# •	Total unique friends
user1 = {"Srushhti","Arya","Aditi","Rahul","Harsh"}
user2 = {"Arya","Vaishnavi","Aditi","siddhi","vedika"}


print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", len(user1 | user2))
