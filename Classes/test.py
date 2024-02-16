import numpy as np
import matplotlib.pyplot as plt

path = "Z:/data_phd_thomas_2023_202x/relaunch_sarocema/AndorCam/022024/09/"
data = np.load(path+'test.npy')
print(np.shape(data))

plt.figure(1)
plt.imshow(data[2])
plt.show()