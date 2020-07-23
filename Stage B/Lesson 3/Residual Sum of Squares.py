import numpy as np
rss = np.sum(np.square(y_test - predicted_values))
round(rss, 3)	    #prints 1.823