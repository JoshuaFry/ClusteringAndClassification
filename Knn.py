import matplotlib.pyplot as plt, random, math, operator


def identify_class(k, x, y, x_s, y_s, class_list):
    # store each distance and its class
    distances = [((math.hypot(x-x_s[i], y-y_s[i])), class_list[i]) for i in range(len(x_s))]

    # obtain k nearest neighbors
    shortest_k_indexes = [distances[i] for i in range(k)]
    for i in range(len(distances)):
        for j in range(len(shortest_k_indexes)):
            if distances[i][0] < shortest_k_indexes[j][0]:
                shortest_k_indexes[j] = distances[i]
                break

    counter = {'r': 0, 'g': 0, 'b': 0, 'k': 0, 'c': 0, 'm': 0}
    for x in range(k):
        if counter[shortest_k_indexes[x][1]]:
            counter[shortest_k_indexes[x][1]] += 1
        else:
            counter[shortest_k_indexes[x][1]] = 1

    highest_count = 0
    temp_class = 'k'
    print(max(counter))
    for x in counter:
        if counter[x] > highest_count:
            highest_count = counter[x]
            temp_class = x

    print(temp_class)
    # plt.scatter(new_data_x,new_data_y, s=99,marker='o',c=temp_class)
    # plt.show()
    return temp_class


def plot_classifiers(x_s,y_s,class_list):
    [plt.scatter(x_s[x],y_s[x],marker='o',c=class_list[x]) for x in range(len(x_s))]
    return


def generate_points(count, min, max):
    return [random.randint(min, max) for x in range(count)]


def generate_radial_points(count, min, max, center_x, center_y, radius):
    points_x = []
    points_y = []
    while len(points_x) < count:
        x = random.randint(min, max)
        y = random.randint(min, max)
        if math.hypot(x - center_x, y - center_y) > radius:
            points_x.append(x)
            points_y.append(y)

    return points_x, points_y


def generate_classes(count, i):
    classes = ['r', 'g', 'b', 'k', 'c', 'm']
    # return [classes[random.randint(0, len(classes)-1)] for x in range(count)]
    return [classes[i] for x in range(count)]


if __name__ == "__main__":

    # Outer region of classifier data
    x_s, y_s = generate_radial_points(80, 0,400, 200, 200, 135)
    class_list = generate_classes(80, 0)

    # Central region of classifier data
    x_s += generate_points(20, 140, 260)
    y_s += generate_points(20, 140, 260)
    class_list += generate_classes(20, 1)

    # training set for class one # red
    training_set_x = [x_s[i] for i in range(64)]
    training_set_y = [y_s[i] for i in range(64)]
    training_set_class = [class_list[i] for i in range(64)]

    # class one's training set
    test_set_x = [x_s[i] for i in range(65, 80)]
    test_set_y = [y_s[i] for i in range(65, 80)]
    test_set_class = [class_list[i] for i in range(65, 80)]

    # training set for class two aka green
    training_set_x += [x_s[i] for i in range(80,95)]
    training_set_y += [y_s[i] for i in range(80,95)]
    training_set_class += [class_list[i] for i in range(80,95)]

    # Class two test set
    test_set_x += [x_s[i] for i in range(95,100)]
    test_set_y += [y_s[i] for i in range(95, 100)]
    test_set_class += [class_list[i] for i in range(95, 100)]

    plt.figure()
    plt.xlabel('Data ooo')
    plt.ylabel('Data Ahh')
    plt.title('KNN')

    plot_classifiers(x_s,y_s,class_list)
    plt.show()

    # Search for K value with highest accuracy rating
    k_s = []
    scores = []
    k = 25
    while k > 0:
        trues = 0
        for i in range(len(test_set_x)):
            c = identify_class(k, test_set_x[i], test_set_y[i], training_set_x, training_set_y, training_set_class)
            # print("classified: " + c + " actual: " + test_set_class[i])
            if c == test_set_class[i]:
                trues += 1
        scores.append(trues/20)
        k_s.append(k)
        k -= 1

    plt.scatter(k_s, scores, marker='o', c='k')
    plt.xlabel('K value')
    plt.ylabel('Percent Accuracy')
    plt.title('KNN Auto-Tune')
    plt.show()
