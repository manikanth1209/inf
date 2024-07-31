import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'http://quotes.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print('Successfully retrieved the webpage')

    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all quote containers
    quotes = soup.find_all('div', class_='quote')

    # Loop through each quote container and extract the text
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

        print(f'Quote: {text}\nAuthor: {author}\nTags: {tags}\n')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
