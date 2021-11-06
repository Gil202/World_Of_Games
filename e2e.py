from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import sys


def test_scores_service():
    theserv=Service("webdrivers/chromedriver.exe")
    browser123 = webdriver.Chrome(service=theserv)
    browser123.get("http://127.0.0.1:8080/")
    sleep(1)
    score_valid = int(browser123.find_element(By.ID, "score").text)
    browser123.close()
    if (score_valid > 1) and (score_valid < 100):
        return True
    else:
        return False


def main_function():
    if test_scores_service():
        return sys.exit(0)
    else:
        return sys.exit(-1)

    
main_function()
