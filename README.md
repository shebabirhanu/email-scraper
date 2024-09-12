# email-scraper
A command-line Python script for crawling through paginated URLs and extracting email addresses. This program saves all retrieved email addresses to a CSV file, saved to your local machine relative to where the script is saved. 

This script is useful for collecting email addresses from directory listings or similar web pages with multiple pages of content.

<img width="1052" alt="Screenshot 2024-09-12 at 4 45 00 PM" src="https://github.com/user-attachments/assets/b3865bf2-c884-4327-a600-b949efb5d774">

# Running the program

1. Install python on your machine.
2. Download the script.
3. Install required packages:
```
pip install requests beautifulsoup4 pandas lxml
```
4. Run the scripts.
5. Follow the prompts and input the `URL` and `number of pages` you would like to crawl. Crawls begin from page 0.
6. Review your .csv file in the file location indicated by the output. 

   
