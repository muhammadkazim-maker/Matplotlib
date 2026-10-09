import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [45000, 52000, 48000, 70000, 65000, 80000, 85000, 90000, 88000, 95000, 105000, 120000]
expenses = [30000, 32000, 31000, 40000, 38000, 45000, 48000, 50000, 49000, 52000, 58000, 62000]



plt.style.use("ggplot")
fig ,ax = plt.subplots(figsize=(10,6))
ax.plot(months,revenue,marker="o",label="Revenue",color="#2b5c8f",linewidth=2.5)
ax.fill_between(months,expenses,alpha=0.3,color="red",label="Expenses")

def currency_fmt(x,pos):
    return f'${int(x/1000)}k'

ax.yaxis.set_major_formatter(ticker.FuncFormatter(currency_fmt))
ax.annotate('Highest Revenue', xy=('Dec', 120000), xytext=('Oct', 130000),arrowprops=dict(facecolor='black', shrink=0.05),fontsize=12, color='black')


ax.set_title("Annual Financial Performance (2026)", fontsize=16, fontweight='bold')
ax.legend(loc='upper left', fontsize=12)
plt.tight_layout()
plt.show()