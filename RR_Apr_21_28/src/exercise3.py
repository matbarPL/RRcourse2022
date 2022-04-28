# Exercise 3

# Write names of all US states in UPPERCASE and lowercase to a file.
# Write how to do this without typing all 50 names manually.
# Separate code from input and from output.
import us
import pandas as pd

us_lower_names = list(map(lambda x: x.lower(),
               us.states.mapping('abbr', 'name').values()))

us_upper_names = list(map(lambda x: x.upper(),
                          us.states.mapping('abbr', 'name').values()))

us_states_df = pd.DataFrame(data = {'lower': us_lower_names,
                                    'upper': us_upper_names})

us_states_df.to_csv('..\\out\\us_states.csv', index = False)
#%%

#%%

#%%

#%%

#%%
