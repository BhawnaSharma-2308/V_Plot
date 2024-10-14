import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('final_frequency.tsv', sep='\t', header=None)
print(data.head())

x = data[0]
y = data[1]
z = data[2]

plt.figure(figsize=(8, 6))
scatter = plt.scatter(x, y, c=z, cmap='magma',s=1, alpha=1)

plt.colorbar(scatter, label='Frequency')

plt.xlabel('Position')
plt.ylabel('Fragment Length')
plt.title('V-Plot')

plt.show()
plt.savefig('v_plot_image1.png')
