import numpy as np
import matplotlib.pyplot as plt

# Rows: Time Slots (6 slots in a day)
# Columns: Days of Week (Mon - Sun)
traffic_data = np.array([
    [ 200,  180,  220,  210,  300,  500,  450],  # 12 AM - 4 AM
    [ 150,  130,  140,  160,  200,  300,  280],  # 4 AM - 8 AM
    [ 850,  900,  880,  920, 1100,  800,  750],  # 8 AM - 12 PM
    [1200, 1250, 1180, 1300, 1600, 1400, 1350],  # 12 PM - 4 PM
    [1500, 1600, 1550, 1700, 2100, 2400, 2200],  # 4 PM - 8 PM (Peak Hours)
    [ 950,  980, 1020, 1100, 1800, 2000, 1750]   # 8 PM - 12 AM
])

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
time_slots = ['12AM-4AM', '4AM-8AM', '8AM-12PM', '12PM-4PM', '4PM-8PM', '8PM-12AM']

# Write your heatmap code below:
fig,ax=plt.subplots(figsize=(10,15))
cmx = ax.imshow(traffic_data, cmap = "coolwarm",aspect="auto")

fig.colorbar(cmx,ax=ax,label = "Active Users (in Thousands)")

ax.set_xticks(range(len(days)))
ax.set_xticklabels(days)
ax.set_yticks(range(len(time_slots)))
ax.set_yticklabels(time_slots)

for i in range (len(time_slots)):
    for j in range(len(days)):
        val = traffic_data[i,j]
        text_color = 'white'if val >= 1800 else "black"
        text_weight = "bold" if val >= 1500 else "normal"
        ax.text(
            j,i,
            str(val),
            ha="center",
            va="center",
            color = text_color,
            fontweight = text_weight,
            fontsize=15
        )

for spine in ax.spines.values():
    spine.set_visible(True)

ax.set_title("E Commerce Mobile App Hourly Traffic and Conversion",color="blue",fontweight= "bold")
# ax.spines["top"].set_visible(False)
# ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()