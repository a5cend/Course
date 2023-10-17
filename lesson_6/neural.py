import random
import numpy as np
import matplotlib.pyplot as plt


class Neural:
    def __init__(self, path_dataset, input_dim=9, output_dim=2, h_dim=25,
                 alpha=0.00001, num_epochs=1000, batch_size=30):

        self.path_dataset = path_dataset
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.h_dim = h_dim
        self.alpha = alpha
        self.num_epochs = num_epochs
        self.batch_size = batch_size
        self.dataset = []
        self.nn_weights = {}

    @staticmethod
    def softmax_batch(t):
        out = np.exp(t)
        return out / np.sum(t, axis=1, keepdims=True)

    @staticmethod
    def sparse_cross_entropy_batch(z, y):
        return -np.log(np.array([z[j, y[j]] for j in range(len(y))]))

    @staticmethod
    def to_full_batch(y, num_classes):
        y_full = np.zeros((len(y), num_classes))
        for j, yj in enumerate(y):
            y_full[j][yj] = 1
        return y_full

    @staticmethod
    def relu(t):
        return np.maximum(t, 0)

    @staticmethod
    def relu_deriv(t):
        return (t >= 0).astype(float)

    def data_preparation(self):
        dataset = np.genfromtxt(self.path_dataset, delimiter=',', dtype=float, skip_header=1)
        for i in range(len(dataset[0]) - 1):
            dataset = dataset[~np.isnan(dataset[:, i])]

        dataset[:, 2] *= 0.001
        dataset[:, 4] *= 0.01
        dataset[:, 5] *= 0.01
        dataset = np.around(dataset, 2)

        target = dataset[:, -1]
        dataset = dataset[:, :9]
        if target.shape[0] != dataset.shape[0]:
            raise Exception('Кол-во строк в таргете и датасете не совпадает!')

        # print(dataset[0])
        self.dataset = [(dataset[i][None, ...], int(target[i])) for i in range(len(target))]


    def inference(selfself, x):
        if not self.nn_weights:
            raise Exception('Сеть не обучена')

        t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
        h1 = self.relu(t1)
        t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
        z = self.softmax_batch(t2)

        return np.argmax(z)


    def calc_accuracy(self):
        correct = 0
        for x, y in self.dataset:
            z = self.inference(x)
            if z == y:
                correct += 1

        return correct / len(self.dataset)


    def training(self):
        self.data_preparation()

        self.nn_weights['W1'] = np.random.rand(self.input_dim, self.h_dim)
        self.nn_weights['b1'] = np.random.rand(1, self.h_dim)
        self.nn_weights['W2'] = np.random.rand(self.h_dim, self.output_dim)
        self.nn_weights['b2'] = np.random.rand(1, self.h_dim)

        self.nn_weights['W1'] = (self.nn_weights['W1'] - 0.5) * 2 * np.sqrt(1 / self.input_dim)
        self.nn_weights['b1'] = (self.nn_weights['b1'] - 0.5) * 2 * np.sqrt(1 / self.input_dim)
        self.nn_weights['W2'] = (self.nn_weights['W2'] - 0.5) * 2 * np.sqrt(1 / self.h_dim)
        self.nn_weights['b2'] = (self.nn_weights['b2'] - 0.5) * 2 * np.sqrt(1 / self.h_dim)

        loss_arr = []

        for ep in range(self.num_epochs):
            random.shuffle(self.dataset)
            for i in range(len(self.dataset) // self.batch_size):
                batch_x, batch_y = zip(*self.dataset[i * self.batch_size: i * self.batch_size + self.batch_size])
                x = np.concatenate(batch_x, axis=0)
                y = np.array(batch_y)

                # Forward
                t1 = x @ self.nn_weights['W1'] + self.nn_weights['b1']
                h1 = self.relu(t1)
                t2 = h1 @ self.nn_weights['W2'] + self.nn_weights['b2']
                z = self.softmax_batch(t2)
                E = np.sum(self.sparse_cross_entropy_batch(z, y))

                # Backward
                y_full = self.to_full_batch(y, self.output_dim)
                dE_dt2 = z - y_full
                dE_dW2 = h1.T @ dE_dt2
                dE_db2 = np.sum(dE_dt2, axis=0, keepdims=True)
                dE_dh1 = dE_dt2 @ self.nn_weights['W2'].T
                dE_dt1 = dE_dh1 * self.relu_deriv(t1)
                dE_dW1 = x.T @ dE_dt1
                dE_db1 = np.sum(dE_dt1, axis=0, keepdims=True)

                # Update
                self.nn_weights['W1'] = self.nn_weights['W1'] - self.alpha * dE_dW1
                self.nn_weights['b1'] = self.nn_weights['b1'] - self.alpha * dE_db1
                self.nn_weights['W2'] = self.nn_weights['W2'] - self.alpha * dE_dW2
                self.nn_weights['b2'] = self.nn_weights['b2'] - self.alpha * dE_db2

                loss_arr.append(E)

        res_acc = self.calc_accuracy()
        print('Accuracy:', res_acc)

        plt.plot(loss_arr)
        plt.savefig('graph_training.png')

