import numpy as np  # This line imports the NumPy library and gives it a short name 'np'

def calculate(list):  # This defines a new function named 'calculate' that takes one input called 'list'
    if len(list) != 9:  # This checks if the input list does not have exactly 9 numbers
        raise ValueError("List must contain nine numbers.")  # If not 9 numbers, show this error message

    values = np.array(list).reshape(3, 3)  # This converts the list into a 3x3 matrix (2D array)

    # Now we create a dictionary to store all the results
    calculations = {
        'mean': [np.mean(values, axis=0).tolist(),   # Mean of each column
                 np.mean(values, axis=1).tolist(),   # Mean of each row
                 np.mean(values).item()],            # Mean of all numbers

        'variance': [np.var(values, axis=0).tolist(),  # Variance of each column
                     np.var(values, axis=1).tolist(),  # Variance of each row
                     np.var(values).item()],           # Variance of all numbers

        'standard deviation': [np.std(values, axis=0).tolist(),  # Std dev of each column
                               np.std(values, axis=1).tolist(),  # Std dev of each row
                               np.std(values).item()],           # Std dev of all numbers

        'max': [np.max(values, axis=0).tolist(),   # Max value in each column
                np.max(values, axis=1).tolist(),   # Max value in each row
                np.max(values).item()],            # Max value in all numbers

        'min': [np.min(values, axis=0).tolist(),   # Min value in each column
                np.min(values, axis=1).tolist(),   # Min value in each row
                np.min(values).item()],            # Min value in all numbers

        'sum': [np.sum(values, axis=0).tolist(),   # Sum of each column
                np.sum(values, axis=1).tolist(),   # Sum of each row
                np.sum(values).item()]             # Sum of all numbers
    }

    return calculations  # This returns the dictionary that has all the results
