import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv(r"D:\spl pro\Titanic histogram.csv")
age_survived = data[data['Survived']==1]['age']
age_not_survived = data[data['Survived'] == 0]['age']
plt.hist(age_survived, color='g', alpha=0.6, label='Survived')
plt.hist(age_not_survived, color='k', alpha=1,label='Not Survived')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Survived and Not Survived Passengers')
plt.legend()
plt.show()