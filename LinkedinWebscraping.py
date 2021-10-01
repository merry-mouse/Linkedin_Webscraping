# importing packages
import pandas as pd
from selenium import webdriver
from time import sleep
from time import time
start_time = time()

# choose jobs, industries and area you are interested in on Linkedin, paste url that you got
url = "https://www.linkedin.com/jobs/search/?f_EA=true&f_I=96%2C4%2C6&f_PP=100495523&f_TPR=r604800&geoId=101165590&keywords=developer%20OR%20engineer%20OR%20architect%20OR%20devops%20OR%20sales%20OR%20support&location=United%20Kingdom&sortBy=R"
# number of jobs you need in your csv file
no_of_jobs = 50

# this will open up new window with the url provided above
# put the path to the driver .exe file in the brackets
driver = webdriver.Chrome("C:/zadachki/Different_Upwork_Projects/chromedriver_win32/chromedriver.exe")
driver.get(url)
sleep(3)
#action = ActionChains(driver)


#scrolling down the page to find necassary number of jobs (25 jobs per page)
i = 2
while i <= int(no_of_jobs/25):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    try:
        driver.find_element_by_xpath("/html/body/div/div/main/section/button").click()
        sleep(5)
    except:
        pass
        print("Searching for more jobs...\n")
        sleep(5)

# getting the list of all jobs
job_lists = driver.find_element_by_class_name("jobs-search__results-list")
jobs = job_lists.find_elements_by_tag_name("li") # return a list
print('You are scraping information about {} jobs.'.format(len(jobs)))

# extract necessary info about each job and storing it into lists
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

    # getting title from the post
    job_title0 = job.find_element_by_css_selector("h3").get_attribute("innerText")
    job_title.append(job_title0)

    # finding companies names
    company_name0 = job.find_element_by_css_selector("h4").get_attribute("innerText")
    company_name.append(company_name0)

    # job location
    job_locations = job.find_element_by_css_selector('span.job-search-card__location').get_attribute("innerText")
    location.append(job_locations)

    # date when posted
    date0 = job.find_element_by_css_selector("div>div>time").get_attribute("datetime")
    date_posted.append(date0)

    # links to each post
    job_link0 = job.find_element_by_css_selector("a").get_attribute("href")
    job_link.append(job_link0)

# checking every link that we scraped before and looking for more additional information
seniority_level = []
employment_type = []
job_function = []
industries = []
for link in job_link:
    url = link
    driver.get(url)
    sleep(5)

    seniority_level0 = driver.find_element_by_xpath(
        "html/body/main/section/div/div/section/div/ul/li[1]/span").get_attribute("innerText")
    seniority_level.append(seniority_level0)

    employment = driver.find_element_by_xpath("html/body/main/section/div/div/section/div/ul/li[2]/span").get_attribute(
        "innerText")
    employment_type.append(employment)

    function = driver.find_element_by_xpath("html/body/main/section/div/div/section/div/ul/li[3]/span").get_attribute(
        "innerText")
    job_function.append(function)

    industry = driver.find_element_by_xpath("html/body/main/section/div/div/section/div/ul/li[4]/span").get_attribute(
        "innerText")
    industries.append(industry)

# writing all the scraped info to a csv file and making a  dictionary of lists
dict = {'Job title': job_title, 'Company name': company_name, 'Location': location, "Date posted": date_posted, "Job link":
        job_link, "Job row": job_row, "Seniority level": seniority_level, "Employment type": employment_type,
        "Job function": job_function, "Industries": industries}

df = pd.DataFrame(dict)

# saving the dataframe to a csv file
df.to_csv("LinkedinJobs.csv", index=False)

