import requests
import sys
from bs4 import BeautifulSoup


def get_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, 'lxml')


def result(user_id):
    url = 'https://stackoverflow.com/users/' + str(user_id) + '?tab=activity&sort=posts&page={}'
    soup = get_soup(url.format('1'))
    total_posts = soup.find('div', {'class': 'subheader user-full-tab-header'}).h1.span.text.replace(',', '').strip()
    posts = soup.find('table', {'class': 'history-table'}).findAll('tr')
    total_pages = int(int(total_posts) / len(posts)) + 1

    links = []
    for page in range(1, total_pages + 1):
        soup = get_soup(url.format(str(page)))
        posts = soup.find('table', {'class': 'history-table'}).findAll('tr')

        for post in posts:
            links.append('https://stackoverflow.com' + post.a['href'])
        break  # remove this to get all posts
        # time.sleep(10)

    return links

if __name__ == '__main__':
    try:
        user_ID = sys.argv[1]
    except IndexError:
        user_ID = None

    result(user_ID)
