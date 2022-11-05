import numpy as np
import pandas as pd
a = np.arange(16)
a = a.reshape(2, 2, 4)
a = a[np.newaxis, :, :, :]
print(a.shape)
