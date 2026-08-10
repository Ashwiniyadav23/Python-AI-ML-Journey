import math_utils

print(math_utils.add(2, 3))      # 5
print(math_utils.square(4))      # 16
print(math_utils.PI)             # 3.14159


# Different ways to import

import math_utils                     # import the whole module
print(math_utils.add(2, 3))

from math_utils import add            # import just one function
print(add(2, 3))

from math_utils import add, square    # import multiple specific things
print(add(2, 3))
print(square(4))

from math_utils import add as sum_two_numbers   # rename on import ("alias")
print(sum_two_numbers(2, 3))

import math_utils as mu               # alias the whole module (very common!)
print(mu.add(2, 3))



# Third-party modules/packages (need installation)

import pandas as pd
data = pd.read_csv("data.csv")