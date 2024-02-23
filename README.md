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
