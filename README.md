# Linkedin webscraping
## (without registration)

This code allows to scrape some basic information about job offers on Linkedin.
Resulting info first stored in separated lists and then in a dictionary and then to a csv file.
# Libraries
You need 3 libraries to be installed for this script to work:

- pandas
- selenium
- time

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
pip install pandas
```
## Usage

there are 3 modules that has to be imported:
- webdriver
- sleep
- time

```python
import pandas as pd
from selenium import webdriver
from time import sleep
from time import time
```
# Variables
There are 3 variables that has to be stated in the beginning of the script:

```python
# linkedin search for jobs you want to scrape
url = "https://www.linkedin.com/jobs/search..."

# number of jobs you need in your csv file
no_of_jobs = 50

# put the path to the driver .exe file in the brackets
driver = webdriver.Chrome("C:/zadachki/Different_Upwork_Projects/...")
```

# Result
Using that dictionary program creates a csv file with following columns:
- Job title
- Company name
- Location
- Date posted
- Job link
- Job row
- Seniority level
- Employment type
- Job function
- Industries

## Contributing
Pull requests are welcome.
