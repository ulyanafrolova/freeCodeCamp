import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr=np.array(numbers).reshape(3,3)
        calculations = {
            "mean" : [list(arr.mean(axis=0)), list(arr.mean(axis=1)), arr.mean()],
            "var" : [list(arr.var(axis=0)), list(arr.var(axis=1)), arr.var()],
            "std" : [list(arr.std(axis=0)), list(arr.std(axis=1)), arr.std()],
            "max" : [list(arr.max(axis=0)), list(arr.max(axis=1)), arr.max()],
            "min" : [list(arr.min(axis=0)), list(arr.min(axis=1)), arr.min()],
            "sum" : [list(arr.sum(axis=0)), list(arr.sum(axis=1)), arr.sum()],
        }
return calculations