import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
covid_data = pd.read_csv("full_data.csv")
covid_data.iloc[0:12:2,:]
Afghanistan_total_cases = covid_data.loc[covid_data['location']=='Afghanistan','total_cases']
print(Afghanistan_total_cases)
world_new_cases = covid_data.loc[covid_data['location']=='World','new_cases']
world_new_cases.mean()
world_new_cases.median()
plt.boxplot(world_new_cases,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
              )
plt.title('new cases worldwide')
plt.show()
world_date = covid_data.loc[covid_data['location']=='World','date']
world_new_deaths = covid_data.loc[covid_data['location']=='World','new_deaths']
plt.plot(world_date, world_new_cases, 'b', world_date, world_new_deaths, 'r')
plt.title('new cases and new deaths worldwide')
plt.show()
Austria_date = covid_data.loc[covid_data['location']=='Austria','date']
Austria_new_cases = covid_data.loc[covid_data['location']=='Austria','new_cases']
plt.plot(Austria_date, Austria_new_cases,'b')
plt.title('new cases developed over time in Australia')
plt.show()
