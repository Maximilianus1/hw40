import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

products = np.array([499256,  20337, 289644,  86648, 976043, 420321, 644902, 455182 ,792308 ,905488, 98236, 379095, 976232, 240981, 533739, 115667, 557237, 796682,  81887, 484145])
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(products)))
fig, (ax,ax2) = plt.subplots(2)
ax.pie(products, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))


min= np.min(products)
max =  np.max(products)
mean = np.mean(products)
average = np.average(products)
median=np.median(products)
summ =np.sum(products)
pos_to_pos_range = np.ptp(products)
products_info =[min,max,mean,average,median,summ,pos_to_pos_range]
x = 0.5 + np.arange(len(products_info))
y=[]
for i in range(len(products_info)):
    y.append(products_info[i]/100000)
ax2.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax2.set(xlim=(0, 8), xticks=np.arange(0, len(products_info)),
       ylim=(0, 8), yticks=np.arange(1,100))

print("max: ",max,"min: ",min,"mean: ",mean,"average: ",average,"median: ",median,"sum: ",summ,"range: ",pos_to_pos_range)
plt.show()