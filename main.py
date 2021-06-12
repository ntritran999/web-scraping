from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time



opts = Options()
opts.add_argument('--ignore-certificate-errors')        # Handle ssl errors.    
opts.add_argument('--ignore-ssl-errors')                
opts.headless = True                                    # Set it to 'True' if you don't want the browser to pop up.
browser = Chrome('./chromedriver.exe', options=opts)    # Path to your chromedriver.
browser.get('https://www.frontendmentor.io/challenges')

source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')

challengecard_contents = soup.find_all('div', class_='ChallengeCard__Content-luiznt-4 kwXWoS')
newbies_links = dict()

for challenge in challengecard_contents:
    name = challenge.find('h3').find('a')
    level = challenge.find('span').text
    if level == '1':
        newbies_links[name.text] = 'https://www.frontendmentor.io' + name['href']

time.sleep(5)
browser.quit()

for title, site in newbies_links.items():
    print(title + ': ' + site, '\n')
