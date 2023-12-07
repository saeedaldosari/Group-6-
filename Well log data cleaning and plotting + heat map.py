import lasio as las
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import missingno as msno
import seaborn as sns

#step 1: describing the data
poro = pd.read_csv('cleaned_data.csv')
data = (las.read('1051661071.las')).df()
desc=data.describe()
data.reset_index(inplace = True)
missing = data.isna().sum()
data = data.dropna()
msno.matrix(data);

#step 2: Cleaning the data
data['RILD'][data['RILD'] > 4000] = np.nan

data['RILM'][data['RILM'] > 4000] = np.nan

data['RLL3'][data['RLL3'] > 4000] = np.nan

data['CNDL'][data['CNDL'] < 0] = np.nan
data['CNDL'][data['CNDL'] > 65] = np.nan

data['DPOR'][data['DPOR'] < 0] = np.nan
data['DPOR'][data['DPOR'] > 100] = np.nan


data['CNLS'][data['CNLS'] < 0] = np.nan

#data['CNPOR'][data['CNPOR'] < 0] = np.nan

data['GR'][data['GR'] > 4000] = np.nan
data['GR'][data['GR'] < 0] = np.nan


data['MCAL'][data['MCAL'] < 0] = np.nan
data['MCAL'][data['MCAL'] > 5000] = np.nan

data['MI'][data['MI'] < 0] = np.nan

data['MN'][data['MN'] < 0] = np.nan


data['RHOB'][data['RHOB'] < 0] = np.nan
data['RHOB'][data['RHOB'] > 15] = np.nan

data['RHOC'][data['RHOC'] <= 0] = np.nan
desc2=data.describe()

dfClean = data[data['GR'] < 35]
dfHC = dfClean[dfClean['RILM'] < 50]

#Step 3: data visualization
fig, axes = plt.subplots(figsize=(10,10))

curve_names = ['Gamma', 'Shallow Res', 'Density', 'Neutron']


#Set up the plot axes
ax1 = plt.subplot2grid((1,3), (0,0), rowspan=1, colspan = 1) 
ax2 = plt.subplot2grid((1,3), (0,1), rowspan=1, colspan = 1)
ax3 = plt.subplot2grid((1,3), (0,2), rowspan=1, colspan = 1)
ax4 = ax3.twiny()

#Set up the individual log tracks / subplots
ax1.plot(data['GR'], data['DEPT'], data , color = "green", lw = 0.5)
ax1.set_xlim(0, 400) 
ax1.spines['top'].set_edgecolor('green')

ax2.plot(data['RLL3'], data['DEPT'], data , color = "black", lw = 0.5)
ax2.set_xlim(0.2, 4000)
ax2.semilogx()
ax2.spines['top'].set_edgecolor('black')

ax3.plot(data['RHOB'], data['DEPT'], data , color = "red", lw = 0.5)
ax3.set_xlim(1, 4.5)
ax3.spines['top'].set_edgecolor('red')


ax4.plot(data['CNPOR'], data['DEPT'], data , color = "blue", lw = 0.5)
ax4.set_xlim(65, -50)
ax4.spines['top'].set_edgecolor('blue')

#Set up the common elements between the subplots
for i, ax in enumerate(fig.axes):
    ax.set_ylim(3000, 2500) # Set the depth range
    
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    ax.set_xlabel(curve_names[i])
    
    if i == 3:
        ax.spines["top"].set_position(("axes", 1.08))
    else:
        ax.grid()
        
#Hide tick labels on the y-axis 
for ax in [ax2, ax3]:
    plt.setp(ax.get_yticklabels(), visible = False)

#Reduce the space between each subplot
fig.subplots_adjust(wspace = 0.05)

plt.show()

#Heat map

dfnew = data[['CNPOR','GR','RHOB','RILD','RILM','RLL3','SP','DEPT']]
cor = dfnew.corr()
plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(dfnew.corr(), cmap= 'RdBu', vmin=-1, vmax=1, annot=True, square =True)
heatmap.set_title('Log Properties Correlation Heatmap', fontdict={'fontsize':12}, pad=12);
