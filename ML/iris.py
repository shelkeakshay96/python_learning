from sklearn.datasets import load_iris

iris = load_iris()

print("Feature names of iris data set")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

for i in range(len(iris.target)):
    print("ID: %d, Features %s, Label : %s" % (i,iris.data[i],iris.target[i]))

















