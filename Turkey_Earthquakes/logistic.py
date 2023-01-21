import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
import seaborn as sns



def logistic_regression_results(train_acc,test_y,y_pred,df):
        
        print("The Accuracy for Training Set is {}".format(train_acc*100))
        test_acc = accuracy_score(test_y, y_pred)
        print("The Accuracy for Test Set is {}".format(test_acc*100))
        print(classification_report(test_y, y_pred))
        # fig, ax = plt.subplots()
        # ax.scatter(test_y, y_pred)
        # ax.plot([test_y.min(), test_y.max()], [test_y.min(), test_y.max()], 'k--', lw=4)
        # ax.set_xlabel('Measured')
        # ax.set_ylabel('Predicted')
        # plt.show()



def logistic_regression(df):
        X = df.iloc[:,[1,2,3,4,5,6,7,8]].values
        Y = df.iloc[:,9].values
        
        #we split the dataset into a test and training set
        X_train, X_test, train_y, test_y = train_test_split(X,Y , test_size=0.3, random_state=0)


        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)


        clf = LogisticRegression(solver='newton-cg')
        clf.fit(X_train, train_y)
        y_pred = clf.predict(X_test)
        da = pd.DataFrame({'Actual': test_y, 'Predicted': y_pred})
        print(da.head(20))

        train_acc = clf.score(X_train, train_y)
        logistic_regression_results(train_acc,test_y,y_pred,df)