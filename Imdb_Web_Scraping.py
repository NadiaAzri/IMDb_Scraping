# Python program to scrape website
# and save all the movies and shows that released in 2020 from imdb
from requests import get
from bs4 import BeautifulSoup
from time import sleep
import time
from random import randint
from IPython.core.display import clear_output
import warnings
import pandas as pd


# Initializing the movies and shows that the loop will populate
all_movies = []
start_time = time.time()
requests = 0
# we'll going to scrape the first 50000 movie and show released in 2020
# For every page (each page has 50 movie and show)
for scr in range(1, 50000, 50):

    # Request from the server the content of the web page by using get(),
    # and store the server’s response in the variable response

    response = get('https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=num_votes,desc&start'
                   '=' + str(scr) + '&ref_=adv_nxt')

    # Pause the loop
    sleep(randint(5, 10))

    # Monitor the requests
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))
    clear_output(wait=True)

    # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warnings.warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(response.text, 'html.parser')

    # Select all the movie containers from the current page
    current_page_movies = page_html.find_all('div', class_='lister-item mode-advanced')

    # For each movie in the current page
    for movie in current_page_movies:
        # Get the info of each movie on the page
        if movie.find('div', class_='ratings-metascore') is not None:
            # The metascore
            metascore = movie.find('span', class_='metascore').text

        else:
            metascore = None
        # The year
        year = movie.h3.find('span', class_='lister-item-year').text
        # The IMDB rating
        imdb = float(movie.strong.text)
        # The name
        name = movie.h3.a.text
        # The number of votes
        vote = movie.find('span', attrs={'name': 'nv'})['data-value']
        # Compiling the movie info
        movie_data = [name, year, imdb, metascore, vote]

        # Append the movie info to the complete dataset
        all_movies.append(movie_data)

all_movies = pd.DataFrame(all_movies,
                          columns=['movie', 'year', 'imdb', 'metascore', 'vote'])
print(all_movies.head(10))
# Cleaning the data
# Convert the values to integers and cleaning the year column.
all_movies['vote'] = all_movies.vote.astype(float)
all_movies['metascore'] = all_movies.metascore.astype(float)
all_movies['imdb'] = all_movies.imdb.astype(float)
all_movies['year'] = all_movies.year.str.extract('(\d+)').astype(float)

print(all_movies.head(10))
all_movies.info()

# Saving the data into a CSV file
all_movies.to_csv('IMDb_data_2020.csv', index=False)

print(all_movies.head(10))

print(all_movies.describe().loc[['min', 'max'], ['imdb', 'metascore']])

