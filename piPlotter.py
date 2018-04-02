import matplotlib.pyplot as plt
 
# Data to plot
labels = 'Neutral', 'Positive', 'Negative'
sizes = [20, 40, 40]
colors = ['lightskyblue','yellowgreen', 'lightcoral']
explode = (0.0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()