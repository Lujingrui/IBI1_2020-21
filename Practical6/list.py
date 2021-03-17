import numpy as np
gene_lengths = np.array([9410, 394141, 4442, 105338, 19149, 76779, 126550, 36296, 842, 15981])
exon_counts = np.array([51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523])
average = gene_lengths/exon_counts
average.sort()
print (average)
import matplotlib.pyplot as plt
plt.boxplot(average,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showcaps = True,
            showfliers = True,
            notch = False
              )
plt.show()
           

