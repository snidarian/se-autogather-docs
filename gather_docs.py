#!/usr/bin/python3

# Setup selenium and Firefox browser
from selenium import webdriver
# Service class and option class fixes
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# import the keys class
from selenium.webdriver.common.keys import Keys

options = Options()

options.profile = '/home/cn1d4r14n/.mozilla/firefox/t8oqdk41.default-esr'

# will eventually run headlessly
options.headless = True

# link to web browser driver
service = Service('/home/cn1d4r14n/Documents/geckodriver')

driver = webdriver.Firefox(options=options, service=service)

# needed to help direct the programs scraping
import argparse
# greater control of terminal from script
import os
# terminal coloring
from colorama import Fore



os.system('jvs -s')



# Searches the document pages with global navbar by exact keyword.
def keyword_search_documents() -> None:
    pass


# Gathers url link document-download-pages one page at a time for X number of document pages
def gather_gathers() -> None:
    pass



def download_linksrows_from_csv(csv_filename) -> None:



def main() -> None:
    pass




if __name__ == "__main__":
    main()





