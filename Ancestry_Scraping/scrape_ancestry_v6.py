# -*- coding: utf-8 -*-
"""
This code scrapes the social security death infromation in the us for a given
death and birth year combination. It is different thatn the previous four
iterations in that it actually scrapes ancestry (not family search.org).

This code will work differently than other scraping ones. There will now be
two seperate python scripts. The first one (this one) will go through
and download all the html source code for each ancestry webpage. It will save
them to a text file. The second piece of code will parse the correct information
and convert them to state readable format.
"""

# Import Libraries
from selenium import webdriver
from time import sleep
import numpy
import os

# Set up the Globals
OUTFILENAME = 'AD_{0}.res'
WRITEPATH = 'H:/Python/ancestry_source'
PATH_TO_WEBDRIVER = 'H:/Python/chromedriver'
C_OPTIONS = webdriver.ChromeOptions()
C_OPTIONS.add_argument("--incognito") # Set up incognito mode
PG1 = 'http://search.ancestry.com/cgi-bin/sse.dll?db=ssdi&gss=angs-d&new=1&rank='
PG2 = '1&MS_AdvCB=1&msbdy=1971&msbdy_x=1&msbdp=10&msddy=2006&msddy_x=1&msdpn__ft'
PG3 = 'p=USA&msdpn=2&msdpn_PInfo=3-%7c0%7c1652393%7c0%7c2%7c0%7c0%7c0%7c0%7c0%7c'
PG4 = '0%7c&msdpn_x=1&msdpn__ftp_x=1&MSAV=2&uidh=000&gl=&gst=&hc=50'
WEBPAGE1 = PG1 + PG2 + PG3 + PG4

# Main function
def main():
    """
    Contains the main logic of the script
    """

    driver = initialize(WEBPAGE1)

    for page in range(1300):

        print page

        try:
            sleep(2  + numpy.random.uniform(7, 13))
            page_source = get_source(driver, page)
            sleep(2 + numpy.random.uniform(7, 13))
            url = next_page(driver, page_source)
            check_feedback(driver)

        except:
            print "Code Failed, Major Exception Raised"
            driver.close()
            driver = initialize(url)
            sleep(800 +  numpy.random.uniform(300, 600))
            page_source = get_source(driver, page)
            sleep(5 + numpy.random.uniform(7, 13))
            url = next_page(driver, page_source)
            check_feedback(driver)

    return 0 # no error return code
# End of main() function

# Initialize the webpage
def initialize(url):
    """
    This function initializes the webpage

    Args:
        -url: The webpage you want to initialize (string).

    Retruns:
        -driver: Chrome webdriver (object).
    """
    driver = webdriver.Chrome(chrome_options=C_OPTIONS,
                      executable_path=PATH_TO_WEBDRIVER)
    driver.implicitly_wait(10)
    driver.get(url) # Get the url

    return driver
# End of initialize() function

# Get the webpage source code
def get_source(driver, identity):
    """
    For each webpage this function takes its source code and writes it to
    a text file.

    Args:
        -driver: The Chrome webdriver (object).
        -identity: The numeric identifier of the page beins scraped (integer).
        
    Retruns:
        -page_source: The html code for the page (string).
    """
    page_source = driver.page_source
    file_name = OUTFILENAME.format(identity)
    print len(page_source) # I want to see how big the source is to monitor odd results

    with open(os.path.join(WRITEPATH, file_name), "w") as outfile:
        outfile.write(page_source)

    #with open(file_name, 'w') as outfile:
    #    outfile.write(page_source)

    return page_source # no error return code
# End of get_source() function

# Move to the next page
def next_page(driver, source):
    """
    This function simply moves the code onto the next page.

    Args:
        -drver: The Chrome webdriver (object).
    Returns:
        -url: The current webpage (atring).
    """
    x_path = '//*[@id="pageSets"]/ul/li[{0}]/a'

    # Find the location of the next page element
    if source.find('<li class="prev">') != -1 and source.find('<li class="next">') != -1:
        # A previous and next element has been found
        start = source.find('<li class="prev">')
        end = source.find('<li class="next">') + 17
        soup = source[start : end]
        list1 = soup.split('<li')
        list_length = len(list1) - 1
        x_path = x_path.format(list_length)
        elem = driver.find_element_by_xpath(x_path)
        elem.click()

    elif source.find('<li class="prev">') == -1 and source.find('<li class="next">') != -1:
        # No previous element exists, but a next one does
        # Therefore, this is the first page
        x_path = x_path.format(5)
        elem = driver.find_element_by_xpath(x_path)
        elem.click()

    elif source.find('<li class="next">') == -1:
        # No next element has been found, which means that we reached the end
        print "Code has finished"

    # Get the page url
    url = driver.current_url
    return url # No error return code
# End of next_page() function
    
# Check if there is a pop-up
def check_feedback(driver):
    """
    This function simply checks if ancestry.com has opened a "We'd welcome
    your feedback" pop-up. It screws up the code.
    """
    x_path = '//*[@id="fsrOverlay"]/div/div/div/div/div/div[2]/div[2]/a'
    try:
        driver.implicitly_wait(3)
        elem = driver.find_element_by_xpath(x_path)
        elem.click()
        driver.implicitly_wait(10)
    except:
        print ""
    return 0 # No error return code
# End of check_feedback() function

# Run the scraping code
if __name__ == '__main__':
    main()
