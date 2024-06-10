
import random
import numpy as np
import matplotlib.pyplot as plt

def randomRange( mn, mx ):
	return mn + (mx - mn) * random.random()

tesadufi = [random.random() for i in range(10000)]
tesadufi_range = [randomRange(18, 90) for i in range(10000)]
tesadufi_gauss = np.random.normal(40, 20, 10000)
# normal distrubiton = gauss distribution



plt.hist(tesadufi, alpha = 0.5)
plt.hist(tesadufi_range, alpha = 0.5)
plt.hist(tesadufi_gauss, alpha = 0.5)

plt.show()