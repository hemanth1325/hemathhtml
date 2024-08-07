import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv('Iris.csv')
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
#y=y.astype('category')
#y=y.cat.codes
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3)
kn=KNeighborsClassifier()
kn.fit(xtrain,ytrain)
ypred=kn.predict(xtest)
#i=0
for label in ytest:
    if label==ypred[i]:
        print('Correct',label)
    else:
        print('Incorrect',label,ypred[i])

acc=accuracy_score(ytest,ypred)
print('accuracy score',acc)