import json
from selenium import webdriver
from bs4 import BeautifulSoup

# Configure Selenium webdriver
driver = webdriver.Chrome()  # Make sure you have the Chrome driver installed and its path set correctly
url = 'https://www2.hm.com/en_in/women/new-arrivals/clothes.html?sort=stock&image-size=small&image=model&offset=0&page-size=436'
driver.get(url)

# Wait for the page to load completely (you might need to adjust the waiting time based on your internet speed)
driver.implicitly_wait(1)

# Get the page source after it has fully loaded
page_source = driver.page_source

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find the <ul> element with class "products-listing small"
product_list = soup.find('ul', class_='products-listing')

# Find all <li> elements within the <ul> element
product_items = product_list.find_all('li', class_='product-item')

# Create a list to store the product information
products = []

# Iterate over the product items
for item in product_items:
    product_name = item.find('a', class_='link').text.strip()
    product_link = item.find('a', class_='link')['href']
    
    # Open the product page
    driver.get('https://www2.hm.com' + product_link)
    
    # Wait for the product page to load completely
    driver.implicitly_wait(1)
    
    # Get the page source of the product page
    product_page_source = driver.page_source
    
    # Create a BeautifulSoup object for the product page
    product_soup = BeautifulSoup(product_page_source, 'html.parser')
    
    # Find the <div> element with class "layout pdp-wrapper product-detail sticky-footer-wrapper js-reviews"
    product_details = product_soup.find('div', class_='layout pdp-wrapper product-detail sticky-footer-wrapper js-reviews')
    
    # Find the <p> element with class "BodyText-module--general__KTCW3 ProductDescription-module--descriptionText__rKCVH BodyText-module--preamble__VwE7e"
    try:
        description_element = product_details.find('p', class_='BodyText-module--general__KTCW3 ProductDescription-module--descriptionText__rKCVH BodyText-module--preamble__VwE7e')
        product_description = description_element.text.strip()
    except AttributeError:
        product_description = "No description available."
    
    # Create a dictionary for the product information
    product_info = {
        'name': product_name,
        'link': 'https://www2.hm.com' + product_link,
        'description': product_description
    }
    
    # Add the product information to the list
    products.append(product_info)

# Close the browser
driver.quit()

# Write the product information to a JSON file
with open('product_info1.json', 'w') as f:
    json.dump(products, f, indent=4)

print('Scraping completed and data saved to product_info.json file.')
