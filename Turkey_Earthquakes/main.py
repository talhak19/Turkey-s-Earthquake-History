import baslangic_sinifi
import pre_process
import linear
import logistic
import kmeans
import graphics

if __name__ == '__main__':

    deprem = baslangic_sinifi.Earthquake("./turkey_earthquakes(1915-2021).csv")
    print("Dataset Info:\n")
    #We get information about Turkey Earthquakes' dataset.
    deprem.data_info(),"\n"

    #You can analyze a column from our dataset.
    # deprem.column_analysis("Mb"),"\n"

    # We need to preprocess our dataset to put in a proper form.
    deprem_pre_process = pre_process.pre_process(deprem)
    
    # We can see the graphics about our dataset
    graphics.show_graphics(deprem_pre_process)
    
    # Using K-means clustering, we cluster and show clusters in the dataset.
    print("\nK-Means process: \n")
    kmeans.Kmeans(deprem_pre_process)

    # Using linear regression, we predict earthquakes and visualize the predictions.
    print("\nLinear regresyon process: \n")
    linear.linear_regression(deprem_pre_process)
    
    #Using logistic regression, we try to predict the location of earthquakes.
    print("\nLogistic regresion process: \n")
    print("Takes some time...")
    
    logistic.logistic_regression(deprem_pre_process)