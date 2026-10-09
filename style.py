# import matplotlib.pyplot as plt 

# print(plt.style.available)


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Apply style before creating figure
plt.style.use('seaborn-v0_8-bright')

# 2. Sample Data
x_vals = [1, 2, 3, 4]
y_vals = [10000, 25000, 50000, 75000]

# 3. Create plot
fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, marker='o')

# 4. Formatter function
def currency_fmt(x, pos):
    return f'${int(x/1000)}k'

# 5. Apply formatter to Y-axis
ax.yaxis.set_major_formatter(ticker.FuncFormatter(currency_fmt))

plt.show()