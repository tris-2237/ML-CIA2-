import pandas as pd

data = pd.read_csv("Student_Marks.csv")

x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.linear_model import LinearRegression
regression = LinearRegression()

regression.fit(x,y)
print(regression.predict([[3,6]])) #to display the prediction in vscode(for our understanding)

#%%
# to make the code abstract and hide from plain view
import pickle
pickle.dump(regression,open('model.pkl','wb'))