# Web-Scraping-Challenge

![img](https://user-images.githubusercontent.com/112406455/208116169-678d4a8b-11bd-46a8-bd03-afbeadf4be0f.png)

## Background
You’re now ready to take on the full web-scraping and data analysis project for the mission to Mars. You’ve learned to identify HTML elements on a page, identify their `id` and class `attributes`, and use this knowledge to extract information via both automated browsing with Splinter and HTML parsing with Beautiful Soup. You’ve also learned to scrape various types of information. These include HTML tables and recurring elements, like multiple news articles on a webpage.

As you work on this Challenge, remember that you’re strengthening the same core skills that you’ve been developing until now: collecting data, organizing and storing data, analyzing data, and then visually communicating your insights.

## What You're Creating
This new assignment consists of two technical products. You will submit the following deliverables:

* Deliverable 1: Scrape titles and preview text from Mars news articles. Optionally export the data into a JSON file or a MongoDB database.

* Deliverable 2: Scrape and analyze Mars weather data, which exists in a table.

## Instructions

### Deliverable 1: Scrape Titles and Preview Text from Mars News

1. Use automated browsing to visit the [Mars NASA news site](https://redplanetscience.com/). Inspect the page to identify which elements to scrape.

<img width="1215" alt="Screenshot 2022-12-19 at 2 09 12 PM" src="https://user-images.githubusercontent.com/112406455/208513559-f890a144-1d45-4948-93f5-58ea5291e7a2.png">

2. Create a Beautiful Soup object and use it to extract text elements from the website.

<img width="1214" alt="Screenshot 2022-12-19 at 2 35 49 PM" src="https://user-images.githubusercontent.com/112406455/208516710-4266661d-bb4a-4216-8a9f-67c3a2d2ecf6.png">

3. Extract the titles and preview text of the news articles that you scraped. Store the scraping results in Python data structures as follows:

* Store each title-and-preview pair in a Python dictionary. And, give each dictionary two keys: `title` and `preview`.

* Store all the dictionaries in a Python list.

<img width="1212" alt="Screenshot 2022-12-19 at 2 20 08 PM" src="https://user-images.githubusercontent.com/112406455/208514077-b3ba6e2b-29b8-4db5-8807-4136ef798a4a.png">

* Print the list in your notebook.

<img width="1214" alt="Screenshot 2022-12-19 at 2 12 08 PM" src="https://user-images.githubusercontent.com/112406455/208514313-c59fa007-a0df-4314-bf0f-3dc2d46115b1.png">

4. Optionally, store the scraped data in a file or database (to ease sharing the data with others). To do so, export the scraped data to either a JSON file or a MongoDB database.

<img width="1212" alt="Screenshot 2022-12-19 at 2 12 15 PM" src="https://user-images.githubusercontent.com/112406455/208514409-af0c0509-1781-450e-8211-750c0645aea0.png">

### Deliverable 2: Scrape and Analyze Mars Weather Data

1. Use automated browsing to visit the [Mars Temperature Data Site](https://data-class-mars-challenge.s3.amazonaws.com/Mars/index.html). Inspect the page to identify which elements to scrape.

<img width="1214" alt="Screenshot 2022-12-19 at 2 25 21 PM" src="https://user-images.githubusercontent.com/112406455/208517361-5649e59c-044f-4afe-9cfd-f206a7b30ed2.png">

2. Create a Beautiful Soup object and use it to scrape the data in the HTML table. Note that this can also be achieved by using the Pandas `read_html` function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

<img width="1214" alt="Screenshot 2022-12-19 at 2 25 32 PM" src="https://user-images.githubusercontent.com/112406455/208517528-e3ddb1f0-6ad6-4ca8-8f61-bed88312461c.png">

3. Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:
  
  * `id`: the identification number of a single transmission from the Curiosity rover

  * `terrestrial_date`: the date on Earth

  * `sol`: the number of elapsed sols (Martian days) since Curiosity landed on Mars

  * `ls`: the solar longitude

  * `month`: the Martian month

  * `min_temp`: the minimum temperature, in Celsius, of a single Martian day (sol)

  * `pressure`: The atmospheric pressure at Curiosity's location

<img width="1213" alt="Screenshot 2022-12-19 at 2 25 40 PM" src="https://user-images.githubusercontent.com/112406455/208517994-e6a3c1ad-9780-4c37-a757-4864be557b5d.png">

<img width="1213" alt="Screenshot 2022-12-19 at 2 25 48 PM" src="https://user-images.githubusercontent.com/112406455/208518109-84caa4b6-25fa-4965-b05a-90b74d089d99.png">

4. Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate `datetime`, `int`, or `float` data types.

<img width="1213" alt="Screenshot 2022-12-19 at 2 26 09 PM" src="https://user-images.githubusercontent.com/112406455/208518618-155f3311-3f3b-4fc7-82d9-72f698bb27f9.png">

5. Analyze your dataset by using Pandas functions to answer the following questions:

* How many months exist on Mars?

<img width="1214" alt="Screenshot 2022-12-19 at 2 26 36 PM" src="https://user-images.githubusercontent.com/112406455/208519182-2887b09b-ab15-4228-94e8-b74e7dcc1952.png">

* How many Martian (and not Earth) days worth of data exist in the scraped dataset?

<img width="1212" alt="Screenshot 2022-12-19 at 2 27 20 PM" src="https://user-images.githubusercontent.com/112406455/208519717-baaaf8be-0ac1-4ef3-a609-c502d3865351.png">

* What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
  
  - Find the average the minimum daily temperature for all of the months.

<img width="1213" alt="Screenshot 2022-12-19 at 2 49 37 PM" src="https://user-images.githubusercontent.com/112406455/208521044-f3309d87-a3b3-442f-bc72-0581e9324d4e.png">

   - Plot the results as a bar chart.

<img width="1212" alt="Screenshot 2022-12-19 at 2 27 30 PM" src="https://user-images.githubusercontent.com/112406455/208522136-d726b4cb-8178-4089-9caf-96311c485cb8.png">

<img width="1212" alt="Screenshot 2022-12-19 at 2 27 40 PM" src="https://user-images.githubusercontent.com/112406455/208521633-c3c117a3-da65-4007-8607-57b95e913324.png">

* Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
  
  - Find the average the daily atmospheric pressure of all the months.

<img width="1212" alt="Screenshot 2022-12-19 at 2 27 50 PM" src="https://user-images.githubusercontent.com/112406455/208522320-393c2d4d-ecaa-44cf-88e6-f4be5c059029.png">

  - Plot the results as a bar chart.

<img width="1213" alt="Screenshot 2022-12-19 at 2 27 58 PM" src="https://user-images.githubusercontent.com/112406455/208522492-75eba640-31d2-4b25-933c-7972a1616c7b.png">

* About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
  
  - Consider how many days elapse on Earth in the time that Mars circles the Sun once.
    
  - Visually estimate the result by plotting the daily minimum temperature.

<img width="1212" alt="Screenshot 2022-12-19 at 2 28 07 PM" src="https://user-images.githubusercontent.com/112406455/208522699-4f3c95ec-155c-4e45-9184-8253a0100be0.png">

6. Export the DataFrame to a CSV file.

<img width="1212" alt="Screenshot 2022-12-19 at 3 00 46 PM" src="https://user-images.githubusercontent.com/112406455/208523224-b9b0d805-a2ff-4703-8a69-e4d894b3d1b5.png">

Code Execution Instructions:


© 2022 edX Boot Camps LLC
