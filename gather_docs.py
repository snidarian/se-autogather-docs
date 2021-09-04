#!/usr/bin/python3

# Setup selenium and Firefox browser
from selenium import webdriver
# Service class and option class fixes
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# For waiting for elements to appear
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import the keys class
from selenium.webdriver.common.keys import Keys

# needed to help direct the programs scraping
import argparse
# greater control of system from script
import os
# terminal coloring
from colorama import Fore
# Argparse to allow various functions to run in different orders
import argparse
import csv
import time


# setup color escape sequences
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET


# SETUP SELENIUM

OPTIONS = Options()

OPTIONS.profile = '/home/cn1d4r14n/.mozilla/firefox/t8oqdk41.default-esr'

# will eventually run headlessly
OPTIONS.headless = False

# link to web browser driver
SERVICE = Service('/home/cn1d4r14n/Documents/geckodriver')

driver = webdriver.Firefox(options=OPTIONS, service=SERVICE)



# Searches the document pages with global navbar by exact keyword.
def keyword_search_box(search_term) -> None:
    driver.get('https://1lib.us/')
    try:
        global_search_bar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchFieldx"]')))
    # Check the 'match words option'
    except:
        print('The global search bar was not located...')
    # Enter search into search bar
    global_search_bar.send_keys(f'{search_term}')
    global_search_bar.send_keys(Keys.RETURN)

# Gathers url link document-download-pages one page at a time for X number of document pages

def gather_urls_on_page() -> list:
    document_metadata = []
    for document_index in range(2, (100 + 1), 2):
        document_title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, f'/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[{document_index}]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a')))
        document_link = driver.find_element_by_xpath(f'/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[{document_index}]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a').get_attribute('href')
        extension_and_size = driver.find_element_by_xpath(f'/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[{document_index}]/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div[2]/div[3]/div[2]')
        document_metadata.append([document_title.text, document_link, extension_and_size.text])
    return document_metadata


def navigate_to_next_results_page() -> None:
    pass


# Takes .csv full URLs and navigates to each one and tries to download it - if it can't be downloaded It calls the change VPN IP function
def download_links_from_csv(csv_filename) -> None:
    with open(f"{csv_filename}", mode="r") as bookurls_csv:
        csv_reader = csv.reader(bookurls_csv, delimiter=',')
        # For loop iterate through all the book URLS in the .csv file
        list_item_count = 1
        for book_link in csv_reader:
            driver.get(f'{book_link[0]}')
            # Find book title text on the book-details page
            book_title = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[1]/div[2]/h1').text
            # attempt the download and respond accordingly if the download is being blocked until IP change
            print(f"{str(list_item_count)}. {YELLOW}{book_title}{RESET} at {GREEN}{driver.current_url}{RESET}")
            link_url = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div[1]/div[1]/div/a').get_attribute('href')
            list_item_count += 1


def change_VPN_IP() -> None:
    print("Changing VPN test statement....")
    os.system('jvs -r')


def main() -> None:
    # Print status of current VPN connection
    os.system('jvs -s')
    # Setup Argparse
    parser = argparse.ArgumentParser(description="Download documents from zlib from the command line and switched VPN IP when necessary")
    args = parser.add_argument("keyword", help="Keyword search term", type=str)
    args = parser.parse_args()
    # from this keyword a [KEYWORD]_documents.csv file is generated and then utilized by other functions in the program
    print(f"Searching for Docs related to keyword: '{args.keyword}'")
    #download_links_from_csv("document_urls.csv")

    keyword_search_box(args.keyword)

    documents_metadata_list = gather_urls_on_page()
    for item in documents_metadata_list:
        print(item)


if __name__ == "__main__":
    main()





