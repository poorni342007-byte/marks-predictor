#import libaries pandas(data handling-using tables), sklearn.linear_model(ml model-linearregression model), joblib(to save the trained model)
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

#create simple dataset
labubu={
    "Hours" : [1,2,3,4,5,6,7,8],
    "Marks" : [20,40,50,60,65,70,80,90]
    }

#converting dictionary to table(data frame) so that internally it looks like excel
df=pd.DataFrame(labubu)

#i/p (user gives)
X=df[["Hours"]]
#o/p (model predicts)
Y=df["Marks"]

#train the model
#create an empty model
model=LinearRegression()

#study the example & learn the patterns
model.fit(X,Y)

#save the model
joblib.dump(model, "model.pk")

#print the message just for confirmation
print("model trained and saved")

#test the model
print(model.predict([[5]]))


