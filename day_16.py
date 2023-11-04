import numpy as np

a : np.ndarray = np.array(1000) # object to store

print(a) # prints
print(a.shape) # prints the shape of the object () = 0 -Denormalized
print(a.dtype) # prints the dtype of the object
print(type(a)) 
print(a.ndim) # prints the number of dimensions
print(a.size) # prints the size of the object
print(a.itemsize) # prints the itemsize of the object



a : np.ndarray = np.array([1,2,3,4]) # object to store [1,2,3,4] = vector

print(f" object {a}") # prints
print(f"object shape {a.shape}") # prints the shape of the object () = 0 -Demoralized
print(f" Object type {a.dtype}") # prints the dtype of the object
print(f"Object type with global function {type(a)}") # prints the dtype of the
print(f"Number of dimension {a.ndim}") # prints the number of dimensions
print(f"Total items in Array : {a.size}") # prints the size of the object
print(f"{a.itemsize}") # prints the item size of the object


import numpy as np

data = [[0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11]]

a : np.ndarray = np.array(data) # object to store [1,2,3,4] = vector

print(f" object {a}") # prints
print(f"objec shape {a.shape}") # prints the shape of the object () = 0 -Denormalized
print(f" Object type {a.dtype}") # prints the dtype of the object
print(f"Object type with global function {type(a)}") # prints the dtype of the
print(f"Number of dimension {a.ndim}") # prints the number of dimensions
print(f"Total items in Array : {a.size}") # prints the size of the object
print(f"{a.itemsize}") # prints the itemsize of the object


ndata : NDArray[Shape["20"], Any] = np.arange(1,21)

print(ndata)
print(ndata.min())
print(ndata.max())
print(ndata.argmax())
print(ndata.argmin)
print(ndata.mean())
print(ndata.std())
print(ndata.sum())
print(ndata.cumsum())