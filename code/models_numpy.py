import numpy as np

# using classes cause it allows us store trained weights and reuse models for multiple predictions
class LogisticRegressionNumPy:
    def __init__(self, learning_rate=0.01, epochs=1000, verbose=False):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.verbose = verbose
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        # clip to prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    # using simple log loss for both models
    def _compute_loss(self, y_true, y_pred):
        epsilon = 1e-15
        # clip to prevent log error
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.random.randn(n_features) * 0.01
        self.bias = 0.0

        for e in range(self.epochs):
            linear_output = X.dot(self.weights) + self.bias
            y_pred = self._sigmoid(linear_output)
            error = y_pred - y
            dw = (1 / n_samples) * X.T.dot(error)
            db = (1 / n_samples) * np.sum(error)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict_proba(self, X):
        linear_output = X.dot(self.weights) + self.bias
        return self._sigmoid(linear_output)

    def predict(self, X):
        probabilities = self.predict_proba(X)
        return (probabilities >= 0.5).astype(int)

class MLPNumPy:
    def __init__(self, hidden_size=64, learning_rate=0.01, epochs=1000, verbose=False):
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.verbose = verbose
        self.W1 = None
        self.b1 = None
        self.W2 = None
        self.b2 = None

    def _relu(self, z):
        return np.maximum(0, z)

    def _relu_derivative(self, z):
        return (z > 0).astype(float)

    def _sigmoid(self, z):
        # clip to prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def _compute_loss(self, y_true, y_pred):
        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # He init performs better
        self.W1 = np.random.randn(n_features, self.hidden_size) * np.sqrt(2.0 / n_features)
        self.b1 = np.zeros(self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, 1) * np.sqrt(2.0 / self.hidden_size)
        self.b2 = np.zeros(1)
        y = y.reshape(-1, 1)

        for epoch in range(self.epochs):
            # forward pass
            z1 = X.dot(self.W1) + self.b1
            a1 = self._relu(z1)
            z2 = a1.dot(self.W2) + self.b2
            a2 = self._sigmoid(z2)

            # backward pass, watch the chain
            dz2 = a2 - y
            dW2 = (1 / n_samples) * a1.T.dot(dz2)
            db2 = (1 / n_samples) * np.sum(dz2, axis=0)
            da1 = dz2.dot(self.W2.T)
            dz1 = da1 * self._relu_derivative(z1)
            dW1 = (1 / n_samples) * X.T.dot(dz1)
            db1 = (1 / n_samples) * np.sum(dz1, axis=0)

            # update weights, descend
            self.W2 -= self.learning_rate * dW2
            self.b2 -= self.learning_rate * db2
            self.W1 -= self.learning_rate * dW1
            self.b1 -= self.learning_rate * db1

    def predict_proba(self, X):
        z1 = X.dot(self.W1) + self.b1
        a1 = self._relu(z1)
        z2 = a1.dot(self.W2) + self.b2
        a2 = self._sigmoid(z2)
        return a2.flatten()

    def predict(self, X):
        probabilities = self.predict_proba(X)
        return (probabilities >= 0.5).astype(int)
