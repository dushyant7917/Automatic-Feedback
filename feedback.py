import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://academia.srmuniv.ac.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&servicename=ZohoCreator&serviceurl=https://academia.srmuniv.ac.in/&service_language=en')

print "Loading signin page..."
print "waiting for 4 secs before sending username and password..."
time.sleep(4)

search = driver.find_element_by_id('Email')
search.send_keys('dushyantsingh_na@srmuniv.edu.in')
search = driver.find_element_by_id('Password')
search.send_keys('pass')
search = driver.find_element_by_id('signinBtn').click()

print "waiting for 4 secs for giving browser time to load the homepage..."
time.sleep(4)

tries = 0
while tries < 10:

    try:
        search = driver.find_element_by_xpath("//td[@pagelinkname='Course_Feedback']").click()
        break

    except Exception as e:
        print e
        print "waiting for 4 secs before trying again..."
        time.sleep(4)
        tries += 1

print "waiting for 10 secs for giving browser time to load the feedback page..."
time.sleep(10)

tries = 0
while tries < 10:

    try:
        search = driver.find_element_by_xpath("//td[@class='resetGridClass']").click()
        for i in search:
            if i.text == "Average":
                i.click()
        break

    except Exception as e:
        print e
        print "waiting for 4 secs before trying again..."
        time.sleep(4)
        tries += 1


search = driver.find_element_by_xpath("//td[@class='zc-button-row']/span/input[@value='Submit']").click()
print "Submit button clicked!"
