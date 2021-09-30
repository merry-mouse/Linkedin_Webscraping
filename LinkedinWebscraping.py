# importing packages
import pandas as pd
import re

from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()

from warnings import warn

# replace variables here.
url = "https://www.linkedin.com/jobs/search/?f_EA=true&f_I=96%2C4%2C6&f_PP=100495523&f_TPR=r604800&geoId=101165590&keywords=developer%20OR%20engineer%20OR%20architect%20OR%20devops%20OR%20sales%20OR%20support&location=United%20Kingdom&sortBy=R"
no_of_jobs = 150

# this will open up new window with the url provided above
driver = webdriver.Chrome("C:/zadachki/Different_Upwork_Projects/chromedriver_win32/chromedriver.exe")
driver.get(url)
sleep(3)
#action = ActionChains(driver)

i = 2
while i <= int(no_of_jobs/25)+1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    try:
        driver.find_element_by_xpath("/html/body/div/div/main/section/button").click()
        sleep(5)
    except:
        pass
        print("Searching for more jobs...\n")
        sleep(5)


job_lists = driver.find_element_by_class_name("jobs-search__results-list")
jobs = job_lists.find_elements_by_tag_name("li") # return a list
print('You are scraping information about {} jobs.'.format(len(jobs)))

job_title = []
company_name = []
location = []
date_posted = []
job_link = []
job_id = []
job_row = []
for job in jobs:
    # jobs's row in the search
    job_row0 = job.find_element_by_css_selector("div").get_attribute("data-row")
    if job_row0 == None:
        job_row0 = job.find_element_by_tag_name("a").get_attribute("data-row")
    job_row.append(job_row0)

    #     # getting title from the post
    job_title0 = job.find_element_by_css_selector("h3").get_attribute("innerText")
    job_title.append(job_title0)

    #     # finding companies names
    company_name0 = job.find_element_by_css_selector("h4").get_attribute("innerText")
    company_name.append(company_name0)

    #     # job location
    job_locations = job.find_element_by_css_selector('span.job-search-card__location').get_attribute("innerText")
    location.append(job_locations)

    #     # date when posted
    date0 = job.find_element_by_css_selector("div>div>time").get_attribute("datetime")
    date_posted.append(date0)

    #     # links to each post
    job_link0 = job.find_element_by_css_selector("a").get_attribute("href")
    job_link.append(job_link0)


seniority_level = []
job_function = []
for link in job_link:
    url = link
    driver.get(url)
    sleep(5)

    seniority_level0 = driver.find_elements_by_css_selector("span.description__job-criteria-text.description__job-criteria-text--criteria")
    for element in seniority_level0:
        try:
            print(element.get_attribute("innerText"))
        except:
            print("Nope")