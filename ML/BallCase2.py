from sklearn import tree

def main():
    rough = 1
    smooth = 0
    ballFeatures = [
        [35, rough],
        [47, rough],
        [90, smooth],
        [48, rough],
        [90, smooth],
        [35, rough],
        [92, smooth],
        [35, rough],
        [35, rough],
        [35, rough],
        [96, smooth],
        [43, rough],
        [110, smooth],
        [35, rough],
        [95, smooth]
    ]
    print('size of dataset : ', len(ballFeatures))
    labels = [
        'Tennis',
        'Tennis',
        'Cricket',
        'Tennis',
        'Cricket',
        'Tennis',
        'Cricket',
        'Tennis',
        'Tennis',
        'Tennis',
        'Cricket',
        'Tennis',
        'Cricket',
        'Tennis',
        'Cricket'
    ]

    obj = tree.DecisionTreeClassifier()     # Decide the algorithem
    trained = obj.fit(ballFeatures, labels)     # Train the model
    print(trained.predict([[106, smooth], [39, rough]])) # Test the model

if (__name__ == '__main__'):
    main()
