import pandas as pd
import numpy as np
import seaborn as sns


titanic = sns.load_dataset("titanic")

print(len(titanic))
print(titanic.info())
print(titanic.describe())

