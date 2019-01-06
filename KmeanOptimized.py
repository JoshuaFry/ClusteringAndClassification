import matplotlib.pyplot as plt, random, math


class Centroid:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.children = []
        self.color = color

    def set_children(self, node):
        self.children.append(node)

    def recalculate_center(self):
        if len(self.children) == 0:
            return
        x_ = [self.children[i].get_x() for i in range(len(self.children))]
        avg_x = sum(x_) / len(x_)
        y_ = [self.children[i].get_y() for i in range(len(self.children))]
        avg_y = sum(y_) / len(y_)
        self.set_x(avg_x)
        self.set_y(avg_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fitness = 999
        self.centroid = Centroid(-999, 999, 'k')
        self.color = 'k'
        self.dist = -999

    def set_centroid(self, centroid):
        self.centroid = centroid

    def set_fitness(self, fitness):
        self.fitness = fitness

    def get_fitness(self):
        return self.fitness

    def get_y(self):
        return self.y

    def get_x(self):
        return self.x

    def set_color(self, color):
        self.color = color

    def set_dist(self, dist):
        self.dist = dist

    def get_dist(self):
        return self.dist

    def find_nearest_centroid(self, centroids):
        colors = ['r', 'g', 'b', 'k', 'c', 'm']
        min_dis = min([(math.hypot(self.x - centroids[i].get_x(), self.y - centroids[i].get_y()), i) for i in range(len(centroids))],
                      key=lambda t: t[0])
        centroids[min_dis[1]].set_children(self)
        #plt.scatter(self.x, self.y, marker='o', c=colors[min_dis[1]])
        self.set_dist(min_dis[0])


def generate_nodes(count):
    return [Node(random.randint(0, 2000),random.randint(0, 2000)) for x in range(count)]


def generate_centroids(count):
    colors = ['r', 'g', 'b', 'c', 'm', 'k']
    return [Centroid(random.randint(0, 2000),random.randint(0, 2000), colors[x % len(colors)]) for x in range(count)]


if __name__ == "__main__":

    k = 1
    fitnesses = []
    ks = []
    nodes = generate_nodes(100)

    while k < 20:
        centroids = generate_centroids(k)

        # [plt.scatter(centroids[i].get_x(), centroids[i].get_y(), marker='^', label='Centroid', s=85., c='k') for i in range(len(centroids))]
        [nodes[i].find_nearest_centroid(centroids) for i in range(len(nodes))]
        [centroids[i].recalculate_center() for i in range(len(centroids))]
        [centroids[i].children.clear() for i in range(len(centroids))]
        [nodes[i].find_nearest_centroid(centroids) for i in range(len(nodes))]


        distances = [nodes[i].get_dist() for i in range(len(nodes))]
        if len(distances) == 0:
            fitnesses.append(0)
        else:
            avg = sum(distances) / len(distances)
            fitnesses.append(avg)

        ks.append(k)
        k += 1
        print("Fitness: " + str(avg))


    plt.scatter(ks, fitnesses, marker='o', c='k')
    plt.xlabel('K value')
    plt.ylabel('Fitness (Avg Distance To Centroid)')
    plt.title('KMeans Auto-Tune')
    plt.show()

