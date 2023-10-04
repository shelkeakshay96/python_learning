from sklearn import tree

def main():
    ballFeatures = [
        [35, 'rough'],
        [47, 'rough'],
        [90, 'smooth'],
        [48, 'rough'],
        [90, 'smooth'],
        [35, 'rough'],
        [92, 'smooth'],
        [35, 'rough'],
        [35, 'rough'],
        [35, 'rough'],
        [96, 'smooth'],
        [43, 'rough'],
        [110, 'smooth'],
        [35, 'rough'],
        [95, 'smooth']
    ]

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

    print(ballFeatures)
    print(labels)

    obj = tree.DecisionTreeClassifier()     # Decide the algorithem
    train = obj.fit(ballFeatures, labels)     # Train the model
    print(train.predict([[96, 'smooth'], [35, 'rough']])) #Error: ValueError: could not convert string to float: 'rough'

if (__name__ == '__main__'):
    main()