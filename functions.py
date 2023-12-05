import numpy as np
import matplotlib.pyplot as plt
from pennylane import numpy as np

def plot_data(x, y, fig=None, ax=None):
    if fig == None:
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    reds = y == 0
    blues = y == 1
    ax.scatter(x[reds, 0], x[reds, 1], c="red", s=10, edgecolor="k")
    ax.scatter(x[blues, 0], x[blues, 1], c="blue", s=10, edgecolor="k")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")


def density_matrix(state):
    return state * np.conj(state).T


def accuracy_score(y_true, y_pred):
    score = y_true == y_pred 
    return score.sum() / len(y_true)


def iterate_minibatches(inputs, targets, batch_size):
    for start_idx in range(0, inputs.shape[0] - batch_size + 1, batch_size):
        idxs = slice(start_idx, start_idx + batch_size)
        yield inputs[idxs], targets[idxs]


