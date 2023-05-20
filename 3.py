from selenium import webdriver
from bs4 import BeautifulSoup

# Configure Selenium webdriver
driver = webdriver.Chrome()  # Make sure you have the Chrome driver installed and its path set correctly
url = 'https://www.myntra.com/clothing?f=Brand%3AAllen%20Solly%2CLevis%2CU.S.%20Polo%20Assn.%3A%3ACategories%3AJackets%2CJeans%2CShirts%2CShorts%2CSweaters%2CSweatshirts%2CTrousers%2CTshirts%3A%3AGender%3Amen%2Cmen%20women&sort=price_desc'
driver.get(url)

# Wait for the page to load completely (you might need to adjust the waiting time based on your internet speed)
driver.implicitly_wait(10)

# Get the page source after it has fully loaded
page_source = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find the <ul> element with class "products-listing small"
product_list = soup.find('ul', class_='results-base')

# Find all <li> elements within the <ul> element
product_items = product_list.find_all('li', class_='product-base')

# Extract the product names and links
for item in product_items:
    product_name = item.find('h4', class_='product-product').text.strip()
    product_link = item.find('a')['href']
    print('Product:', product_name)
    print('Link:', 'https://www.myntra.com/'+ product_link)
    print('-----------------------------')

# Close the browser
driver.quit()
