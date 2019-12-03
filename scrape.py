from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#launch url
url = 'https://artsexperiments.withgoogle.com/artpalette/colors/851740-226819-b43eb4-112814-aa7930'

# create a new Chrome session
print('Opening the url')
driver = webdriver.Chrome(executable_path=r'C:\Users\jfields\Desktop\Code\Picture-Palette\chromedriver.exe')
driver.implicitly_wait(5)
driver.get(url)

# parse the html using beautiful soup and store in variable `soup`
print('pulling the html')
soup = BeautifulSoup(driver.page_source, 'html.parser')

# close page
print('closing the driver')
driver.quit()