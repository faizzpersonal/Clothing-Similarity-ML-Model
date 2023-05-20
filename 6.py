import json
from selenium import webdriver
from bs4 import BeautifulSoup

# Configure Selenium webdriver
driver = webdriver.Chrome()  # Make sure you have the Chrome driver installed and its path set correctly
base_url = 'https://www.myntra.com/clothing?f=Brand%3AAllen%20Solly%2CDressBerry%2CLevis%2CTrendyol%2CU.S.%20Polo%20Assn.%3A%3ACategories%3ADresses%2CJackets%2CJeans%2CShirts%2CShorts%2CSweaters%2CSweatshirts%2CTops%2CTrousers%2CTshirts%3A%3AGender%3Amen%20women%2Cwomen&sort=price_desc'

# Define the number of pages you want to scrape (e.g., 239)
num_pages = 10

# List to store the product data
products = []

for page in range(1, num_pages + 1):
    # Create the URL for each page
    url = f'{base_url}&p={page}'
    print(page)
    # Load the page
    driver.get(url)

    # Wait for the page to load completely (you might need to adjust the waiting time based on your internet speed)
    driver.implicitly_wait(1)

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

        # Open the product page
        driver.get('https://www.myntra.com/' + product_link)
    
        # Wait for the product page to load completely
        driver.implicitly_wait(1)
    
        # Get the page source of the product page
        product_page_source = driver.page_source
    
        # Create a BeautifulSoup object for the product page
        product_soup = BeautifulSoup(product_page_source, 'html.parser')
    
        # Find the <div> element with class "layout pdp-wrapper product-detail sticky-footer-wrapper js-reviews"
        product_details = product_soup.find('div', class_='pdp-productDescriptorsContainer')
    
        # Find the <p> element with class "BodyText-module--general__KTCW3 ProductDescription-module--descriptionText__rKCVH BodyText-module--preamble__VwE7e"
        try:
            description_element = product_details.find('p', class_='pdp-product-description-content')
            product_description = description_element.text.strip()
        except AttributeError:
            product_description = "No description available."
    
        # Store the product data in a dictionary
        product_data = {
            'name': product_name,
            'link': 'https://www.myntra.com/' + product_link,
            'description': product_description
        }
        
        # Append the product data to the products list
        products.append(product_data)

# Close the browser
driver.quit()

# Save the product data to a JSON file
with open('products1.json', 'w') as file:
    json.dump(products, file, indent=4)
