import matplotlib.pyplot as plt, random, math, operator

def identify_class(k, x, y, x_s, y_s, class_list):
    distances = [((math.hypot(x-x_s[i], y-y_s[i])), class_list[i]) for i in range(len(x_s))] #store each distance and its index
    shortest_k_indexs = [distances[i]for i in range(k)]
    for i in range(len(distances)): #obtain k nearest neighbors
        for j in range(len(shortest_k_indexs)):
            if distances[i][0] < shortest_k_indexs[j][0]:
                shortest_k_indexs[j] = distances[i]

    counter = {'r':0,'g':0,'b':0,'k':0,'c':0,'m':0}
    for x in range(k): #count each class in shortest lists
        if counter[shortest_k_indexs[x][1]]:
            counter[shortest_k_indexs[x][1]] +=1
        else:
            counter[shortest_k_indexs[x][1]] = 1

    highest_count = 0
    temp_class = 'k'
    for x in counter:
        if counter[x] > highest_count:
            highest_count = counter[x]
            temp_class = x
    plt.scatter(new_data_x,new_data_y, s=99,marker='o',c=temp_class)
    plt.show()



def plot_classifiers(x_s,y_s,class_list):
    [plt.scatter(x_s[x],y_s[x],marker='o',c=class_list[x]) for x in range(len(x_s))]
    return

def generate_points(count, min, max):
    return [random.randint(min, max) for x in range(count)]

def generate_classes(count, i):
    classes = ['r','g','b','k','c','m']
    #return [classes[random.randint(0, len(classes)-1)] for x in range(count)]
    return [classes[i] for x in range(count)]

if __name__ == "__main__":
    x_s = generate_points(100, 0, 400)
    y_s = generate_points(100, 0, 400)
    class_list = generate_classes(100, 0)

    x_s += generate_points(200, 270, 500)
    y_s += generate_points(200, 270, 500)
    class_list += generate_classes(200, 1)

    x_s += generate_points(150, 100, 900)
    y_s += generate_points(150, 100, 900)
    class_list += generate_classes(150, 2)

    plt.figure()
    plt.xlabel('Data ooo')
    plt.ylabel('Data Ahh')
    plt.title('KNN')

    plot_classifiers(x_s,y_s,class_list)
    plt.show()

    new_data_x = random.randint(300, 400)
    new_data_y = random.randint(300, 400)
    plot_classifiers(x_s,y_s,class_list)
    plt.scatter(new_data_x,new_data_y,s=99, marker='o',c='k')
    plt.show()
    plot_classifiers(x_s,y_s,class_list)
    identify_class(4, new_data_x, new_data_y, x_s, y_s, class_list)

