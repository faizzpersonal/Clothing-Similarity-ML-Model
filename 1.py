from selenium import webdriver
from bs4 import BeautifulSoup

# Configure Selenium webdriver
driver = webdriver.Chrome()  # Make sure you have the Chrome driver installed and its path set correctly
url = 'https://www2.hm.com/en_in/men/new-arrivals/clothes.html?sort=stock&image-size=small&image=model&offset=0&page-size=288'
driver.get(url)

# Wait for the page to load completely (you might need to adjust the waiting time based on your internet speed)
driver.implicitly_wait(10)

# Get the page source after it has fully loaded
page_source = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find the <ul> element with class "products-listing small"
product_list = soup.find('ul', class_='products-listing')

# Find all <li> elements within the <ul> element
product_items = product_list.find_all('li', class_='product-item')

# Extract the product names and links
for item in product_items:
    product_name = item.find('a', class_='link').text.strip()
    product_link = item.find('a', class_='link')['href']
    print('Product:', product_name)
    print('Link:', 'https://www2.hm.com'+ product_link)
    print('-----------------------------')

# Close the browser
driver.quit()
