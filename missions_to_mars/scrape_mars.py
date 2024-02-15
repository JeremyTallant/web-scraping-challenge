# scrape_mars.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from io import StringIO

# Function to initialize and return the WebDriver
def initialize_webdriver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

# Function to fetch and display an image from a given URL
def fetch_image_url(url, css_selector="img.wide-image", base_url="https://astrogeology.usgs.gov"):
    driver = initialize_webdriver()
    try:
        driver.get(url)
        image_element = driver.find_element(By.CSS_SELECTOR, css_selector)
        image_src = image_element.get_attribute('src')
        image_url = base_url + image_src if image_src.startswith('/') else image_src
    except Exception as e:
        print(f"An error occurred: {e}")
        image_url = None
    finally:
        driver.quit()
    return image_url

def scrape():
    scraped_data = {}

    # Initialize WebDriver
    driver = initialize_webdriver()

    # NASA Mars News
    try:
        url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.item_list li.slide")))
        articles = driver.find_elements(By.CSS_SELECTOR, "ul.item_list li.slide")
        news = [{'title': article.find_element(By.CSS_SELECTOR, "div.content_title").text,
                 'details': article.find_element(By.CSS_SELECTOR, "div.article_teaser_body").text} for article in articles]
        scraped_data['news'] = news
    finally:
        driver.quit()

    # Mars Featured Image
    driver = initialize_webdriver()
    try:
        url = "https://mars.nasa.gov/mars2020/multimedia/raw-images/image-of-the-week/"
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        image_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.main_image img")))
        scraped_data['featured_image'] = image_element.get_attribute('src')
    finally:
        driver.quit()

    # Mars Facts
    driver = initialize_webdriver()
    try:
        url = "https://mars.nasa.gov/all-about-mars/facts/"
        driver.get(url)
        table_html = driver.find_element(By.CSS_SELECTOR, "table.mb_table").get_attribute('outerHTML')
        df = pd.read_html(StringIO(table_html))[0]
        df.columns = ['Metric', 'Earth', 'Mars']
        scraped_data['mars_facts'] = df.to_dict('records')
    finally:
        driver.quit()

    # Mars Hemisphere Images
    image_urls = [
        "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced",
        "https://astrogeology.usgs.gov/search/details/Mars/Viking/syrtis_major_enhanced/tif#:~:text=Mosaic%20of%20the%20Syrtis%20Major,in%20an%20point%20perspective%20projection.",
        "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced",
        "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced#:~:text=Mosaic%20of%20the%20Valles%20Marineris,6km%2Fpixel."
    ]
    hemisphere_images = [fetch_image_url(url) for url in image_urls]
    scraped_data['hemisphere_images'] = hemisphere_images

    return scraped_data

if __name__ == "__main__":
    result = scrape()
    print(result)
