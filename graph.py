import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
year = data['year']
pop = data['pop']
base = 55000
toppop = 75000
topyear = 2050
pre2022, post2022, poppre, poppost = [], [], [], []
for i in range(len(year)):
    if year[i] < 2022:
        pre2022.append(year[i])
        poppre.append(pop[i])
    elif year[i] == 2022:
        pre2022.append(year[i])
        post2022.append(year[i])
        poppre.append(pop[i])
        poppost.append(pop[i])
    else:
        post2022.append(year[i])
        poppost.append(pop[i])

plt.plot(post2022, poppost, color='#444444', linestyle='--')
plt.plot(pre2022, poppre, color='#444444',)
plt.plot(topyear, toppop)

plt.fill_between(year, pop, base, where=(year <= 2022), color='lightblue', label ='Actual growth from 2000 to 2022')
plt.fill_between(year, pop, base, where=(year >= 2022), color='lightgray', label='Predicted growth from 2022 to 2050')

plt.yticks(range(base,75001, 5000))
plt.legend(loc='upper left')
plt.ylabel('population (000s)', labelpad=15)
plt.grid(linewidth=0.3)
plt.margins(x=0, y=0)
plt.show()