#pip install pandas pip install trafilatura

import pandas as pd
from trafilatura import fetch_url, extract

# define Url's

urltoscrap = ["https://agodino.es",
              "https://www.google.com"]

content = []

#implement scrapping and saving content

for url in urltoscrap:
    urlscrapped = fetch_url(url)
    contentt = extract(urlscrapped ,include_comments=None, include_links=None, incude_tables=None)
    print(f"\n CONTENT  from: {url}")
    print(contentt)

    content.append(contentt)

#Create csv

pd.DataFrame(list(zip(urltoscrap, content)), columns=["URL", "Content"]).to_csv("C:/Scrapping/scrappedthing.csv", index=False)
