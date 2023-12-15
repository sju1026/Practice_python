import pandas as pd
import matplotlib.pyplot as plt

movieData = pd.read_csv('data.csv')

print(movieData)

print(movieData['average'].count())

#년도별 평균
movieData['year'] = pd.DatetimeIndex(movieData['년도']).year
means = movieData.groupby('year').mean()
means['average'].plot(kind = 'bar', color = 'red')

# 상세 평균
avg = movieData[['년도', 'average']]
avg_group = avg.groupby('년도').sum()

plt.figure(figsize = (40, 15))
plt.xlabel('year')
plt.ylabel('avg')
avg_group['average'].plot(kind = 'bar', color = 'blue')
avg_group['average'].plot(color = 'red', marker = 'o', linewidth = 5.0)