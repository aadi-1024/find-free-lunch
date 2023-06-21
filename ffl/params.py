#prebuild gridsearch models

RandomForest = {
        'n_estimators': [10, 50, 100, 250, 500, 1000],
        'max_depth': [None, 10, 50, 100, 250],
}

KNeighbors = {
    'n_neighbors': [1, 3, 5, 10, 25, 100, 500, 1000],
}

SVC = {
    'C': {0.2, 0.5, 1.0, 2.5, 5.0, 10.0, 50.0, 100.0},
}

