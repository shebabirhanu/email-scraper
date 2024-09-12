import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
import os

# get base URL from user w/o page num
input_url = input("Please enter the URL to scrape: ")

modified_url = input_url[:-1] # remove page number/last character

# get number of pages to scrape from user
num_pages = int(input("Please enter the number of pages to scrape: "))

for page in range(num_pages): 
    #append page num to URL
    parse_url = modified_url + str(page) 

    req = requests.get(parse_url) 
    unscraped = deque([parse_url])  #flag for while loop
    scraped = set()  
    emails = set()  

    while len(unscraped):
        url = unscraped.popleft()  
        scraped.add(url)

        parts = urlsplit(url)

        # handle base URLs   
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        if '/' in parts.path:
          path = url[:url.rfind('/')+1]
        else:
          path = url

        print("Crawling URL %s" % url)
        try:
            response = requests.get(url) # send GET request to URL
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue
        
        # regex to find emails in page's content
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.+[a-z0-9\.\-+_]", response.text, re.I))
        emails.update(new_emails) 

        #parse page contents
        soup = BeautifulSoup(response.text, 'lxml')

        for anchor in soup.find_all("a"):
          if "href" in anchor.attrs:
            link = anchor.attrs["href"]
          else:
            link = ''

            if link.startswith('/'):
                link = base_url + link
            
            elif not link.startswith('http'):
                link = path + link

            if not link.endswith("."):
              if not link in unscraped and not link in scraped:
                  unscraped.append(link)
        # save emails to csv 
        df = pd.DataFrame(emails, columns=["Email"])
        filename = 'emails.csv'
        df.to_csv(filename, mode='a', index=False)


# print file location
file_path = os.path.join(os.getcwd(), filename)
print(f"Crawl complete. File saved in location: {file_path}")