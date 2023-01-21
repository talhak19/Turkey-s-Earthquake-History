import pandas as pd


import warnings
warnings.filterwarnings('ignore')

class Earthquake:

    def __init__(self,data):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        self.df = pd.read_csv(data, delimiter=';')
    
    def data_info(self):
        print("Rows and Columns number:\n",self.df.shape)
        print("-------------------------------------------------------------------------------------------")
        print("\nDataFrame Head:\n",self.df.head())
        print("-------------------------------------------------------------------------------------------")
        print("\nData info:"),self.df.info()
        print("-------------------------------------------------------------------------------------------")
        print("Missing value Check:\n",self.df.isnull().sum(),"\n")
        print("-------------------------------------------------------------------------------------------")
        #Sayısal değerli sütunların analizi
        print(self.df.describe())
        print("-------------------------------------------------------------------------------------------")

    def column_analysis(self,column):
        #Here we check there is a column name is exist or not in our dataset
        try:
            grouped_data = self.df[column]
            print(grouped_data.describe())
        except:
            print("There is no column with this name.")
