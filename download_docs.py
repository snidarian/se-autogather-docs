#!/usr/bin/python3


import os
import csv
import time
import argparse
from colorama import Fore


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


# SETUP SELENIUM

OPTIONS = Options()

OPTIONS.profile = '/home/cn1d4r14n/.mozilla/firefox/t8oqdk41.default-esr'

# will eventually run headlessly
OPTIONS.headless = False

# link to web browser driver
SERVICE = Service('/home/cn1d4r14n/Documents/geckodriver')

driver = webdriver.Firefox(options=OPTIONS, service=SERVICE)


# Ansi terminal color escape sequences
RED = Fore.RED
BLUE = Fore.BLUE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET


# At the heart of this program is the vpn switch function which I have to make intelligent and simple
# If the vpn fails to connect, then the program either needs to try the connection again or terminate.
# The boolean this function returns tells the calling function whether or not the VPN change was successful or not
def change_vpn() -> bool:
    exit_code = os.system('jvs -r')
    if exit_code == 0:
        return True
    else:
        return False


# given the input of a link, the function navigate to the link and attempt to download the document found there by the .click() method
# based on whether it was successful or not it will return a boolean, change the vpn and try again
def download_document_at_link(document_link) -> bool:
    # try except statement here that returns True if it can download the link and False if it can't
    driver.get(document_link)
    try:
        download_link = WebDriverWait(driver, 12).until(EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div[1]/div[1]/div/a')))
        print(download_link)
        print(type(download_link))
        time.sleep(3)
    except:
        print("ELEMENT NOT LOCATED")



def main() -> None:
    # Set up argparse 
    parser = argparse.ArgumentParser(description="Downloads (or attempts to) all links in the target formatted .csv")
    args = parser.add_argument("linkfile", help=".csv link source-file", type=str)
    args = parser.parse_args()

    vpn_change_success = change_vpn()
    if vpn_change_success == True:
        print("VPN change was successful")
    else:
        print("VPN Change was unsuccessful")
    
    # The below csv reader will cycle through all the available links in the .csv
    with open(f"{args.linkfile}", mode="r") as linkfile:
        link_reader = csv.reader(linkfile, delimiter=',')
        for row in link_reader:
            document_title = row[0]
            document_download_url = row[1]
            print(f"Downloading {GREEN}{document_title}{RESET} from {YELLOW}{document_download_url}{RESET}")
            download_document_at_link(document_download_url)


if __name__ == "__main__":
    main()



