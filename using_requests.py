import requests as r
from bs4 import BeautifulSoup


source = r.get('https://www.frontendmentor.io/challenges').content
soup = BeautifulSoup(source, 'html.parser')

challengecard_contents = soup.find_all('div', class_='ChallengeCard__Content-luiznt-4 kwXWoS')
newbies_links = dict()

for challenge in challengecard_contents:
    name = challenge.find('h3').find('a')
    level = challenge.find('span').text
    if level == '1':
        newbies_links[name.text] = 'https://www.frontendmentor.io' + name['href']

for title, site in newbies_links.items():
    print(title + ': ' + site, '\n')
