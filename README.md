# ClusteringAndClassification

This repo contains two seperate auto-tuning clustering algorithms, K-Means, and K-Nearest-Neighbors. 
The Auto-Tuning is done to find the most optimal performing value of K for each algorithm. 

Kmeans.py is the only one that does not auto-tune and is a pure K-Means algorithm that will set 3 random centroids
into the data set. Upon closing the first graph the centroids will recalculate their centers within their current cluster and
all the data points are re-classified based of the closest centroid. This step is done 3 times and produces one final graph.

