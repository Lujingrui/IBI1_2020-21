# Set up the dictionary
genes = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
print(genes)
import matplotlib.pyplot as plt
# The following steps set basic information about the pie chart.
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
explode = (0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
plt.axis('equal') 
plt.title('coronavirus infection rates')
plt.show()


