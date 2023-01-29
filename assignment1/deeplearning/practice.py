import numpy as np

x = np.ones((3,3,3))
x[0,1,2] = 3        
out = np.zeros(3,)
out[:] = np.max(x,axis=(0,1)) 
print(out)