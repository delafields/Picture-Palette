from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re

#launch url
url = 'https://artsexperiments.withgoogle.com/artpalette/colors/851740-226819-b43eb4-112814-aa7930'

# create a new Chrome session
print('Opening the url')
driver = webdriver.Chrome(executable_path=r'C:\Users\jfields\Desktop\Code\Picture-Palette\chromedriver.exe')
driver.implicitly_wait(10)
driver.get(url)

# parse the html using beautiful soup and store in variable `soup`
print('pulling the html')
soup = BeautifulSoup(driver.page_source, 'html.parser')

# palette
palette_soup = soup.find('ul', attrs={'class': 'palette'})

color_soup = palette_soup.find_all('li')
colors = []
rgb = re.compile('rgb\((\d+),\s*(\d+),\s*(\d+)\)')

def extract_rgb_convert_hex(string):
    string = str(string)
    result = rgb.findall(string)[0]
    result = tuple(int(num) for num in result)
    hex_result = '#%02x%02x%02x' % result
    return hex_result

for color in color_soup:
    c = extract_rgb_convert_hex(color)
    colors.append(c)

print(c)

# close page
print('closing the driver')
driver.quit()