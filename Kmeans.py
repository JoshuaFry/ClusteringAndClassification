import matplotlib.pyplot as plt, random, math


def generate_points(count):
    #pts = [Point.Point(random.randint(0,201), random.randint(0,501)) for x in range(count)]
    return [random.randint(0, 2000) for x in range(count)]


def generate_point():
    return random.randint(0,2000)


#find the closest centeroid for a given point x,y and change its color
def find_nearest_centroid(x,y, centroids_x, centroid_y):
    colors = ['r','g','b','k','c','m']
    min_dis = min([(math.hypot(x-centroids_x[i], y-centroid_y[i]), i) for i in range(len(centroid_y))], key=lambda t: t[0])
    plt.scatter(x,y,marker='o',c=colors[min_dis[1]])
    print(min_dis)
    return [x,y,min_dis[1]]


def recalculate_centroids(x_list, y_list, centroid_list, centroids_x, centroids_y):
    for t in range(len(centroids_y)):
        x_ = [x_list[i] for i in range(len(x_list)) if centroid_list[i] == t]
        avg_x = sum(x_)/len(x_)
        y_ = [y_list[i] for i in range(len(y_list)) if centroid_list[i] == t]
        avg_y = sum(y_) / len(y_)
        centroids_x[t] = avg_x
        centroids_y[t] = avg_y
    return [centroids_x, centroids_y]


if __name__ == "__main__":
    colors = ['r','g','b','k','c','m']
    x_coord = generate_points(500)
    y_coord = generate_points(500)
    centroids_x = [generate_point() for x in range(3)]
    centroids_y = [generate_point() for x in range(3)]
    centroids_scale = [5 for x in range(3)]

    plt.figure()
    plt.xlabel('Data ooo')
    plt.ylabel('Data Ahh')
    plt.title('K- Means')

    #save a parallel list of x,y, and centroids to determine new centroid postitions
    xycentroid_list = [find_nearest_centroid(x_coord[i], y_coord[i], centroids_x,centroids_y) for i in range(len(x_coord))]

    x_list = [xycentroid_list[i][0] for i in range(len(xycentroid_list))]
    y_list = [xycentroid_list[i][1] for i in range(len(xycentroid_list))]
    centroids_list = [xycentroid_list[i][2] for i in range(len(xycentroid_list))]

    plt.scatter(centroids_x, centroids_y, marker='^', label='Centroid', s=85., c='k')
    plt.axis([0,2000,0, 2000])

    plt.show()

    #Recalculate Centroids for i iterations
    for i in range(3):
        centroids_new = recalculate_centroids(x_list, y_list, centroids_list, centroids_x, centroids_y)
        centroids_x = centroids_new[0]
        centroids_y = centroids_new[1]
        [find_nearest_centroid(x_coord[i], y_coord[i], centroids_x,centroids_y) for i in range(len(x_coord))]
    plt.scatter(centroids_x, centroids_y, marker='^', label='Centroid', s=85., c='k')

    plt.show()