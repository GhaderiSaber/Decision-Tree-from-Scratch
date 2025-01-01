#  write your code here
import pandas as pd

df = pd.read_csv('data/dataset/input.txt')

value_means = df.pivot_table(index='labels',
                               values=['null_deg', '60_deg', "90_deg", "180_deg", "240_deg"],
                               aggfunc='mean')

print(value_means.loc['R', 'null_deg'].round(2))

