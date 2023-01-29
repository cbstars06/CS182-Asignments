import numpy as np

probs = np.ones((4,5))
probs[0,0] = 0
probs[1,1] = 0
print(probs)
y = np.array([0,1,2,3])
print(y)
N = 4
print([np.arange(N),y])
print(probs[np.arange(N),y])

