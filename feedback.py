import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

driver = webdriver.Firefox()
driver.get('https://academia.srmuniv.ac.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&servicename=ZohoCreator&serviceurl=https://academia.srmuniv.ac.in/&service_language=en')

print "Loading signin page..."
print "waiting for 5 secs before sending username and password..."
time.sleep(5)

search = driver.find_element_by_id('Email')
search.send_keys('dushyantsingh_na@srmuniv.edu.in')
search = driver.find_element_by_id('Password')
search.send_keys('account password')
search = driver.find_element_by_id('signinBtn').click()

print "waiting for 20 secs to give browser the time to load the homepage..."
time.sleep(20)

tries = 0
while tries < 10:

    try:
        print "Choosing the feedback form from navbar..."
        search = driver.find_element_by_xpath("//td[@pagelinkname='Course_Feedback']").click()
        break

    except Exception as e:
        print e
        print "waiting for 5 secs before trying again..."
        time.sleep(5)
        tries += 1

print "waiting for 20 secs to give browser the time to load the feedback page..."
time.sleep(20)

tries = 0
while tries < 10:

    try:
        print "finding all the select menu(s)..."
        search = driver.find_elements_by_xpath('//td[@elname="zc-fieldtd"]/div[@class="flLeft"]/div[@class="zc-searchlookup-div zc-searchlookup-div-singleselect"]/li[@class="search-selected-val "]')
        if len(search) > 0:
            break

    except Exception as e:
        print e
        print "waiting for 5 secs before trying again..."
        time.sleep(5)
        tries += 1

print "filling the feedback form begins..."
for i in xrange(17, 129):
    search[i].click()
    random_value = randint(1, 5)
    while random_value > 0:
        search[i].send_keys(Keys.ARROW_DOWN)
        random_value -= 1
    search[i].send_keys(Keys.ENTER)


for i in xrange(144, 183):
    search[i].click()
    random_value = randint(1, 5)
    while random_value > 0:
        search[i].send_keys(Keys.ARROW_DOWN)
        random_value -= 1
    search[i].send_keys(Keys.ENTER)

print "submitting the feedback form..."
search = driver.find_element_by_xpath("//td[@class='zc-button-row']/span/input[@value='Submit']").click()
print "Submit button clicked!"
