import pandas as pd

penguin_sample = {'species': {0: 'Gentoo', 1: 'Adelie', 2: 'Gentoo', 3: 'Gentoo', 4: 'Adelie', 5: 'Adelie',
                              6: 'Adelie', 7: 'Gentoo', 8: 'Chinstrap', 9: 'Gentoo', 10: 'Gentoo', 11: 'Chinstrap',
                              12: 'Adelie', 13: 'Adelie', 14: 'Gentoo', 15: 'Adelie', 16: 'Adelie', 17: 'Gentoo', 
                              18: 'Adelie', 19: 'Gentoo'},
                  'island': {0: 'Biscoe', 1: 'Dream', 2: 'Biscoe', 3: 'Biscoe', 4: 'Torgersen', 5: 'Dream',
                             6: 'Torgersen', 7: 'Biscoe', 8: 'Dream', 9: 'Biscoe', 10: 'Biscoe', 11: 'Dream', 
                             12: 'Torgersen', 13: 'Dream', 14: 'Biscoe', 15: 'Torgersen', 16: 'Biscoe', 17: 'Biscoe', 
                             18: 'Torgersen', 19: 'Biscoe'},
                  'flipper_length_mm': {0: 226.0, 1: 187.0, 2: 229.0, 3: 222.0, 4: 180.0, 5: 182.0, 6: 190.0, 7: 208.0,
                                        8: 196.0, 9: 211.0, 10: 230.0, 11: 202.0, 12: 191.0, 13: 190.0, 14: 214.0,
                                        15: 184.0, 16: 203.0, 17: 210.0, 18: 191.0, 19: 212.0}}

df = pd.DataFrame(penguin_sample)

# your code here
comp_results = df.groupby(['island', 'species'])['flipper_length_mm'].sum()
print(comp_results)