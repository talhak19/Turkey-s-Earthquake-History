import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import statsmodels.api as sm
import numpy as np



def _graphic_after_regression(df):
        df1 = df.head(25)
        df1.plot(kind='bar',figsize=(16,10))
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.title("Linear Regression Graphic")
        plt.show()
        

def linear_regression(df):
        X = df[["Enlem","Boylam","Derinlik","MD","ML","Ms","Mb"]]
        y = df["xM"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        regr = LinearRegression()  
        regr.fit(X_train, y_train) #training the algorithm
       
        coeff_df = pd.DataFrame(regr.coef_, X.columns, columns=['Coefficient'])
        print(coeff_df)

        y_pred = regr.predict(X_test)
        da = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
        print(da.head(10))
        _graphic_after_regression(da)
        olsmod = sm.OLS(df['xM'], X).fit()
        print(olsmod.summary())
        print('R2 score:', olsmod.rsquared)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

