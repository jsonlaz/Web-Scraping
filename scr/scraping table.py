# Scraping Data from a Website + Pandas

from bs4 import BeautifulSoup
import requests

# Wikipedia page URL
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

print(soup)

soup.find_all('table')

soup.find_all('table')[0]

table = soup.find_all('table', class_ = "wikitable sortable")[0]

print(table)

table.find_all('th')

world_title = table.find_all('th')

world_title

world_table_title = [title.text.strip() for title in world_title]

print(world_table_title)

import pandas as pd

df = pd.DataFrame(columns = world_table_title)

df

column_data = table.find_all('tr')

for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'C:\Users\Aterbruket\OneDrive\Documents\Raw Dataset\companies.csv', index = False)
