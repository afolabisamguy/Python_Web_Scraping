import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# URL of the LinkedIn job search page
url = "https://www.linkedin.com/jobs/search/?keywords=python%20developer&location=Lagos%20State%2C%20Nigeria"

# Set up Selenium webdriver (Chrome)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the job search page
driver.get(url)

# Wait for the page to load (adjust the delay as needed)
time.sleep(5)

# Get the page source after JavaScript rendering
page_source = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find the job listing containers
job_listings = soup.find_all("div", class_="base-card")

# Loop through each job listing
for job_listing in job_listings:
    # Extract the job title
    job_title = job_listing.find("h3", class_="base-search-card__title").text.strip()

    # Extract the company name
    company_name = job_listing.find("h4", class_="base-search-card__subtitle").text.strip()

    # Extract the job location
    job_location = job_listing.find("span", class_="job-search-card__location").text.strip()

    # Extract the job description
    job_description = job_listing.find("div", class_="base-search-card__description").text.strip()

    # Print the extracted job details
    print("Job Title:", job_title)
    print("Company:", company_name)
    print("Location:", job_location)
    print("Description:", job_description)
    print("------------------------------")

# Close the webdriver
driver.quit()