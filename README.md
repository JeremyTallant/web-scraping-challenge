# Mission to Mars: A Web-Scraping Journey
![image](images/mars.png)
## Background
This project presents a sophisticated web application designed to bring the forefront of Martian exploration directly to your screen. By harnessing the capabilities of Python, the application meticulously scrapes various scientific websites to gather the latest data on Mars missions. The back-end foundation is built with Flask, a micro web framework that efficiently routes and renders the collected data. At the same time, MongoDB is the backbone for data storage, ensuring the information is current and persistently available. The result is a user-friendly platform that educates and inspires by providing up-to-the-minute insights into our neighboring planet's exploration with the convenience of a single, intuitive interface. 
## Objective
This project aims to create an advanced web application that consolidates and displays the latest data from Mars exploration missions. Leveraging a suite of Python libraries encapsulated in a Jupyter Notebook titled `mission_to_mars.ipynb`; the application initiates the data acquisition process. This operation is conducted with the help of `Selenium`, which enables programmatic navigation of web pages to scrape content effectively. Using the `webdriver` and accompanying modules from `Selenium` facilitates the automation of browser interactions, including retrieving up-to-date news, full-size images, and detailed Mars facts.

Data scraping involves acquiring the latest news from the NASA Mars News Site, featuring titles and paragraph text, and obtaining the current featured Mars image from JPL's space images archive. Additionally, tabular data about Mars, such as diameter and mass, are extracted from the Mars Facts webpage and converted into HTML table strings using `pandas`. High-resolution images and information for Mars's hemispheres are captured and organized using Python dictionaries.

Post data collection, the project transitions to its next phase, which involves displaying the scraped data via a web application developed with Flask and MongoDB. This segment includes the transformation of the Jupyter Notebook into a Python script, `scrape_mars.py`, which contains a `scrape` function. This function is then invoked through a `/scrape` route within the Flask application to update the Mars data in the MongoDB database. The root route `/` renders the aggregated data into an HTML template, `index.html`, designed to present the information in a user-friendly format.

Dependencies like `ChromeDriverManager` ensure the automated scraping process is executed with an up-to-date browser driver, and `StringIO` is utilized for efficient in-memory string processing. This project aims to offer an educational and engaging experience for users interested in Mars exploration by showcasing the efficacy of web scraping techniques in gathering and presenting diverse web content.
## File Descriptions
```text
missions_to_mars/
├── app.py                      
├── scrape_mars.py              
├── mission_to_mars.ipynb       
├── templates/                  
│   └── index.html              
└── static/                     
    └── css/                    
        └── styles.css
```
This web application comprises several essential files that work together to scrape, process, and display Mars exploration data. Below is a breakdown of each file and its role within the project:
* `mission_to_mars.ipynb`: This Jupyter Notebook is the starting point for our scraping process. It uses Python and libraries like Selenium to automate data collection from various sources. The notebook contains detailed comments explaining each step of the scraping procedure, making it easy for others to understand and modify the code if needed.
* `scrape_mars.py`: Derived from the Jupyter Notebook, this Python script encapsulates the scraping logic into a `scrape()` function. When executed, it gathers the latest Mars exploration data and returns it as a Python dictionary, ready for storage in MongoDB.
* `app.py`: This is the Flask application's main file. It defines the server routes that handle requests from the web interface. The `/scrape` route triggers the `scrape()` function from `scrape_mars.py` and updates the database with fresh data. The root route `/` queries the database and populates the `index.html` template with the Mars data for display.
* `index.html`: Located within the `templates` folder, this HTML file is the application's front end. It is designed to structure and display the scraped data in a user-friendly format. The template includes placeholders dynamically filled with data from the MongoDB database when the Flask app renders it.
* `styles.css`: Situated within the `static` folder, this Cascading Style Sheet (CSS) file is responsible for the styling of the web application. It defines the visual appearance of the HTML elements on the webpage, ensuring that the Mars data presentation is engaging and accessible.
## Implementation
In the Implementation section of our Mars Exploration Web Application, we meticulously outline the step-by-step process and methodologies employed to bring this project from concept to reality, detailing the integration of data scraping, backend development, and frontend presentation.
### Jupyter Notebook
#### Selenium Web Scraping Setup
```python
# Dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from IPython.display import Image, display
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from io import StringIO
```
This code initializes a Selenium WebDriver for Chrome using `ChromeDriverManager`, enabling automated web scraping and data handling with `pandas`, and supports image display in IPython environments. 
#### Web Scraping and Image Display with Selenium
```python
# Function to initialize and return the WebDriver
def initialize_webdriver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

# Function to fetch and display an image from a given URL
def fetch_and_display_image(url, css_selector="img.wide-image", base_url="https://astrogeology.usgs.gov"):
    # Call initialize_webdriver() to get a WebDriver instance
    driver = initialize_webdriver()
    
    try:
        # Navigate to the website
        driver.get(url)
        
        # Extract the image src
        image_element = driver.find_element(By.CSS_SELECTOR, css_selector)
        image_src = image_element.get_attribute('src')
        
        # Construct the absolute URL
        image_url = base_url + image_src if image_src.startswith('/') else image_src
        
        # Close the driver
        driver.quit()
        
        # Display the image in the notebook
        display(Image(url=image_url))
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # Ensure the driver is closed even if an exception occurs
        driver.quit()
```
This code includes two functions for web scraping using Selenium: `initialize_webdriver` initializes a Chrome WebDriver, and `fetch_and_display_image` fetches and displays an image from a specified URL using a CSS selector.
#### Extracting Latest Mars News with Selenium
```python
# Call initialize_webdriver() to get a WebDriver instance
driver = initialize_webdriver()

# Navigate to the website
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
driver.get(url)

# Wait for the page to load and titles to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.item_list li.slide")))

# Retrieve titles and details
articles = driver.find_elements(By.CSS_SELECTOR, "ul.item_list li.slide")
for article in articles:
    title = article.find_element(By.CSS_SELECTOR, "div.content_title").text
    details = article.find_element(By.CSS_SELECTOR, "div.article_teaser_body").text
    print(f"Title: {title}\nDetails: {details}\n")

# Close the driver
driver.quit()
``` 
This script uses Selenium to navigate to NASA's Mars news website, waits for the news articles to load, and then scrapes the titles and summaries of the latest articles, printing each to the console. It demonstrates explicit waits to ensure elements are visible before interaction and clean resource management by closing the WebDriver after execution.