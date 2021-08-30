# Python program to scrape website
# and save all the movies that released in 2020 from imdb
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('/home/nadia/PycharmProjects/Web_Scraping/IMDb_data_2020.csv')


ratings = sum(i > 8.0 for i in df['imdb']), \
          sum(6.0 < i < 8.0 for i in df['imdb']), \
          sum(5.0 < i < 6.0 for i in df['imdb']), \
          sum(3.0 < i < 5.0 for i in df['imdb']), \
          sum(i < 3.0 for i in df['imdb'])
meta_score = sum(i > 90.0 for i in df['metascore']), \
             sum(80 < i < 90.0 for i in df['metascore']), \
             sum(60.0 < i < 80.0 for i in df['metascore']), \
             sum(50.0 < i < 60.0 for i in df['metascore']), \
             sum(30.0 < i < 50.0 for i in df['metascore']), \
             sum(i < 30.0 for i in df['metascore'])

print(meta_score)
activities = ['rate > 8.0', '6.0 < rate < 8.0', '5.0 < rate < 6.0', '3.0 < rate < 5.0', 'rate < 3.0']
labels = ['meta_score > 90', '80 < meta_score < 90', '60 < meta_score < 80', '50 < meta_score < 60',
          '30 < meta_score < 50', 'meta_score < 30']

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors_rates = ['r', 'y', 'g', 'b', 'c']

# plotting the pie chart
plt.pie(ratings, colors=colors_rates,
        startangle=90, shadow=True, explode=(0, 0, 0, 0, 0),
        radius=1.2, autopct='%1.0f%%')
# plotting legend
plt.legend(activities)
plt.title('2020\'s movies and shows imdb rates')
# showing the plot
plt.show()

colors_score = ['red', 'orange', 'green', 'purple', 'cyan', 'brown']

# plotting the pie chart
plt.pie(meta_score, colors=colors_score,
        startangle=90, shadow=True, explode=(0, 0, 0, 0, 0, 0),
        radius=1.2, autopct='%1.0f%%')
# plotting legend
plt.legend(labels)
plt.title('2020\'s movies and shows metascores')
# showing the plot
plt.show()

left = [1, 2, 3, 4, 5]

# plotting a bar chart
plt.bar(left, ratings, tick_label=activities,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('Rates')
# naming the y-axis
plt.ylabel('Number of movies and shows')
# plot title
plt.title('2020\'s movies and shows imdb rates')

# function to show the plot
plt.show()

