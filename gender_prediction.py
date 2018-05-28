from sklearn import tree;
from sklearn.neighbors import KNeighborsClassifier;
import numpy as np;

#[height,weight,shoe size]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],
     [166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],
     [171,75,42],[181,85,43]];
print("size of x = "+str(np.shape(X)));

Y = ['male','female','female','female','male','male',
     'male','female','male','female','male'];
print("size of y = "+str(np.shape(Y)));

clf1 = tree.DecisionTreeClassifier();
clf1 = clf1.fit(X,Y);
prediction1 = clf1.predict([[190,70,43]]);
print(prediction1);

clf2 = KNeighborsClassifier(n_neighbors=3);
clf2 = clf2.fit(X,Y);
prediction2 = clf2.predict([[190,70,43]]);
print(prediction1);
