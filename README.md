# web_scrap_udemy_coupon
Scrap all the udemy links from learnviral website and store in excel
Using Webscraping method this code will get the html code of the website.

Initially using python requests module getting the URL content.
Using BeautifulSoup it converts to soup object.
Using Soup.findall fetching the html tag by giving tag name and class it is using.
Then a list of html tags are created.
By iterating the list fetching the hyperlinks and storing into a list format.

Convert into dataframe and then to excel using pandas module.
