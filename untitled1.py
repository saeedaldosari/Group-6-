import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import pylab 
import scipy.stats as stats
df = pd.read_csv('cleaned_data.csv')
stats.probplot(df['Porosity (%)'], dist='norm',plot=pylab)
plt.title('Porosity Probability Plot')
pylab.show()

stats.probplot(df['Permeability (mD)'], dist='norm',plot=pylab)
plt.title('Permeability Probability Plot')
pylab.show()

df['Porosity (%)'].hist()
plt.xlabel('Porosity')
plt.ylabel('Frequency')
plt.title('Porosity Histogram')
plt.show()

df['Permeability (mD)'].hist()
plt.xlabel('Permeability')
plt.ylabel('Frequency')
plt.title('Permeability Histogram')
plt.show()

