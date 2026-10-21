import matplotlib.pyplot as plt

events = [[1, 2, 3, 5], [2, 4, 6]]
plt.eventplot(events, orientation="horizontal")
plt.title("Event Plot")
plt.xlabel("Event Position")
plt.show()
