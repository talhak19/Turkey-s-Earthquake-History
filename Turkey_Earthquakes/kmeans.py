import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

  
def graphic(kmeans,y_kmeans,df,x1):

        centroid_1, centroid_2,centroid_3,centroid_4 = kmeans.cluster_centers_
        centroid_1 = np.delete(centroid_1,2)
        centroid_2 = np.delete(centroid_2,2)
        centroid_3 = np.delete(centroid_3,2)
        centroid_4 = np.delete(centroid_4,2)
        sns.scatterplot(x=df["Derinlik"], y=df["Enlem"], hue = df["ClusterNo"] ,palette='Set1',
                size=df["xM"], sizes=(20,200), 
                    legend = 'brief')
        plt.legend(loc=2, bbox_to_anchor=(0.80, 1.19))

        plt.scatter(centroid_1[1],centroid_1[0],color="yellow")
        plt.scatter(centroid_2[1],centroid_2[0],color="yellow")
        plt.scatter(centroid_3[1],centroid_3[0],color="yellow")
        plt.scatter(centroid_4[1],centroid_4[0],color="yellow")
        plt.axis('off')
        plt.show()
        plt.scatter(x1[y_kmeans==0, 0], x1[y_kmeans==0, 1], s=100, c='red', label ='Cluster 1')
        plt.scatter(x1[y_kmeans==1, 0], x1[y_kmeans==1, 1], s=100, c='blue', label ='Cluster 2')
        plt.scatter(x1[y_kmeans==2, 0], x1[y_kmeans==2, 1], s=100, c='green', label ='Cluster 3')
        plt.scatter(x1[y_kmeans==3, 0], x1[y_kmeans==3, 1], s=100, c='cyan', label ='Cluster 4')


        centers =kmeans.cluster_centers_
        plt.scatter(centers[:, 0], centers[:, 1], s=300, c='yellow', label = 'Centroids')
        plt.title('Clusters of Customers')
        plt.show()



def elbow(df):
        inertia = []
        for n in range(1 , 11):
            algorithm = (KMeans(n_clusters = n ,init='k-means++', n_init = 10 ,max_iter=300, 
                                tol=0.0001,  random_state= 111  , algorithm='full') )
            algorithm.fit(df)
            inertia.append(algorithm.inertia_)
        plt.figure(1 , figsize = (15 ,6))
        plt.plot(np.arange(1 , 11) , inertia , 'o')
        plt.plot(np.arange(1 , 11) , inertia , '-' , alpha = 0.5)
        plt.xlabel('Number of Clusters') , plt.ylabel('Inertia'), plt.title("Elbow Method for K-Means")
        plt.show()



def Kmeans(df):

        x1 = df[['Enlem','Derinlik',"xM"]].iloc[: , :].values
        elbow(x1)
        kmeans = (KMeans(n_clusters=4).fit(x1))
        labels1 = kmeans.labels_
        df['ClusterNo'] = labels1

        y_kmeans = kmeans.fit_predict(x1) 
        print("Inertia: ",kmeans.inertia_)
        for i in range(4):
            print(f"cluster {i + 1} contains: {np.sum(y_kmeans == i)} customers")

        graphic(kmeans,y_kmeans,df,x1)