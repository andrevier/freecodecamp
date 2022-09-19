'''
Example of web scraping for a job position at linkedin.
This method needs the web page of the post and not the search page, where you 
search for open positions. First, you have to search the position. Once you 
found it, you copy the link and paste it in the variable called post_link. 
Then, the code follows the link with the webdriver and get the main 
informations, such as: Job title, Company, Place, and descriptions.

Log in is an option.

You can change the web driver to other browsers, such as Firefox.

You can extend this version to get other informations if you like.
DD-MM-YY
18/09/22
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


if __name__ == '__main__':
  # Use the chrome drive that is in this path.
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
  # Login 
  # EMAIL = 
  # PASSWORD = 
  
  #driver.get("https://www.linkedin.com/uas/login")
  #time.sleep(3)


  #driver.find_element(By.ID, "username").send_keys(EMAIL)
  #driver.find_element(By.ID, "password").send_keys(PASSWORD)
  #driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
  
  # Locate info from job posts.
  post_link = "https://www.linkedin.com/jobs/view/3233151332/"
  sleep_time = 4

  driver.get(post_link)
  time.sleep(sleep_time)
  
  # Get the page's content in html with the driver and assign it to 
  # BeautifoulSoup obj to parse.
  content = driver.page_source
  soup = BeautifulSoup(content, 'html.parser')
  
  # Close the browser.
  driver.close()

  # Open a .txt file to print all the important features:
  # Job position, Enterprise name, place and the job description.
  job_title_selector = "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"
  job_title_selector_type = 'class'
  job_title_selector_tag = 'h1'

  company_selector = "topcard__org-name-link topcard__flavor--black-link"
  company_selector_type = 'class'
  company_selector_tag = 'a'
  
  place_selector = "topcard__flavor topcard__flavor--bullet"
  place_selector_type = 'class'
  place_selector_tag = 'span'
  
  criteria_selector = "description__job-criteria-text description__job-criteria-text--criteria"
  criteria_selector_type = 'class'
  criteria_selector_tag = 'span'

  post_selector = "show-more-less-html__markup show-more-less-html__markup--clamp-after-5"
  post_selector_type = 'class'
  post_selector_tag = 'div'
  
  with open('job_post.txt', 'w', encoding='utf-8') as f:
    # Job title
    for data in soup.findAll(job_title_selector_tag, { job_title_selector_type: job_title_selector}):
      f.write(data.string.lstrip() + '\n')
    
    # Company
    for data in soup.findAll(company_selector_tag, {company_selector_type, company_selector }):
      f.write(data.string.lstrip() + '\n')
    
    # Place
    for data in soup.findAll(place_selector_tag, {place_selector_type, place_selector}):
      f.write(data.string.lstrip() + '\n')

    for data in soup.findAll(criteria_selector_tag, {criteria_selector_type, criteria_selector}):
      f.write(data.string.lstrip() + '\n')
    
    # Post link
    f.write(post_link + '\n')

    # Post
    for elem in soup.findAll(post_selector_tag, {post_selector_type, post_selector}):
      for p in elem.findAll('p'):
        print(p.string)
        if p.string == None:
          f.write('\n')
        else:
          f.write(p.string)
          f.write('\n')

  