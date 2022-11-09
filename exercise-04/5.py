# For this exercise, you shouldn't need to commit code, but you need to verify that your installation is working as expected. Please install the libraries numpy, scikit-learnand pandas.

# You can use the code in 5.py to test your installation. If everything works, you should see something like this:

# [[0. 0. 0.]
#  [0. 0. 0.]]
# Survived    int64
# dtype: object
#   (0, 276)	1
#   (0, 446)	1
#   (0, 1156)	1
#   (0, 2114)	1
#   (0, 2851)	1
#   (0, 3167)	1
#   (0, 4113)	1
#   (0, 4555)	1
#   (0, 4905)	1
# Please pay attention for error messages or exceptions!

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Test NumPy
print(np.zeros((2, 3)))

# Test Pandas
titanic = pd.read_csv("titanic.csv")
print(titanic.dtypes[1:2])

# Test scikit-learn
fo = open("wiki.txt", encoding="UTF-8")
lines = [line for line in fo.readlines()]
fo.close()

vectorizer = CountVectorizer(max_features=5000)
vectorizer.fit(lines)
vectors = vectorizer.transform(lines)
print(vectors[1])

# unable to verify hence numpy req pip which wont install cause conda not existing which isnt even supposed to be on windows. I retreat....'
#
# can confirm
#[[0. 0. 0.]
# [0. 0. 0.]]
# as output though. seems like titanic.csv is missing in our files
#