import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('vgsales.csv')
data.head()

drop_row_index = data[data['Year'] > 2015].index
data = data.drop(drop_row_index)
data['Genre'].value_counts()
sns.countplot(x="Genre", data=data, order = data['Genre'].value_counts().index)
plt.xlabel('Genre of the game')
plt.ylabel('Sales by genre')
plt.xticks(rotation=90)
