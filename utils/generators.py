# List of numpy functions that generate an output sequence
from numpy.lib.stride_tricks import as_strided
import numpy as np

def partial_brnn(xdata, batch_size, num_batches, extra_data=None):
    vocab = extra_data["vocab"]
    seq_length = extra_data["seq_length"]
    back_steps = extra_data["back_steps"]

    space = vocab[' ']
    new_x = np.lib.pad(xdata, (back_steps-1, 0), mode='constant', constant_values=space)
    ydata = np.copy(xdata)
    ydata[:-1] = xdata[1:]
    ydata[-1] = xdata[0]
    x_batches = as_strided(new_x,
                           shape=(new_x.size//seq_length, seq_length + back_steps - 1),
                           strides=(new_x.strides[0]*seq_length, new_x.strides[0]))
    x_batches = np.split(x_batches.reshape((batch_size, -1)), num_batches, 1)
    y_batches = np.split(ydata.reshape(batch_size, -1), num_batches, 1)
    return x_batches, y_batches

def next_char_char(xdata, batch_size, num_batches, extra_data=None):
    ydata = np.copy(xdata)
    ydata[:-1] = xdata[1:]
    ydata[-1] = xdata[0]
    x_batches = np.split(xdata.reshape(batch_size, -1), num_batches, 1)
    y_batches = np.split(ydata.reshape(batch_size, -1), num_batches, 1)
    return x_batches, y_batches

def same_char_char(xdata, extra_data=None):
    ydata = np.copy(xdata)
    x_batches = np.split(xdata.reshape(batch_size, -1), num_batches, 1)
    y_batches = np.split(ydata.reshape(batch_size, -1), num_batches, 1)
    return x_batches, y_batches

def same_ipa_char(xdata, extra_data=None):
    ydata = np.copy(extra_data)
    x_batches = np.split(xdata.reshape(batch_size, -1), num_batches, 1)
    y_batches = np.split(ydata.reshape(batch_size, -1), num_batches, 1)
    return x_batches, y_batches

def next_ipa_ipa(xdata, extra_data=None):
    ydata = np.copy(xdata)
    ydata[:-1] = xdata[1:]
    ydata[-1] = xdata[0]
    x_batches = np.split(xdata.reshape(batch_size, -1), num_batches, 1)
    y_batches = np.split(ydata.reshape(batch_size, -1), num_batches, 1)
    return x_batches, y_batches