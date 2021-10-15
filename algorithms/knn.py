# Original source:
# https://youtu.be/ngLyX54e1LU
# https://twitter.com/python_engineer/status/1446484038970130432?s=20

from collections import Counter
import numpy as np


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(x1 - x2) ** 2)


class Knn:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute distances between x an all exmples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indexes of the first k neighbors - argsort uses quicksort by default, O(n * logn)
        k_idx = np.argsort(distances)[: self.k]
        # Extract the labels of the k nearest neighbors training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]


model = Knn(k=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)