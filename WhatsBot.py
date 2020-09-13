from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import Football_API
import time


msg = Football_API.data()
#function called when user_name is not in the directory/new chat
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = browser.find_element_by_xpath('user input required')#eg.//*[@id="side"]/div[1]/div/label
    new_chat.click()
    # Enter the name of chat
    new_user = browser.find_element_by_xpath('user input required')#eg.//div[@class="_3FRCZ copyable-text selectable-text"]
    new_user.send_keys(user_name)
    time.sleep(1)
    try:
        # Select for the title having user name
        user = browser.find_element_by_xpath('user input required'.format(user_name))#eg.//span[@title="{}"]
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        browser.close()
        browser.quit()
        sys.exit()

#opens the automated chrome window
options = webdriver.ChromeOptions()
#user only has to login the first time
#takes user login data from the brower cache and stores it in a folder
options.add_argument('--user-data-dir= C:/user/location to/store cache')#eg. C:/Users/Lenovo/source/repos/WhatBot/data
#Location for brower cache
options.add_argument('--profile-directory=Default')
options.add_argument('---no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#Executable path for chrome driver
browser = webdriver.Chrome(executable_path ='C:/Users/Loction for/chromedriver',options = options )#eg .C:/Users/Lenovo/source/repos/WhatBot/chromedriver
browser.get('https://web.whatsapp.com/')

#to give time for scanning of code
time.sleep(20)



names = ["Insert Contact name","or names"]
for name in names:
    #finds the name of the contac in the directory
    try:
        user = browser.find_element_by_xpath('user input required'.format(name))#//span[@title="{}"]
        user.click()
    except NoSuchElementException as se:
        new_chat(name)
    time.sleep(5)
    #clicking chat box
    message_box = browser.find_element_by_xpath('user input required')#//div[@class = "_3uMse"]
    message_box.click()
    #typing message
    for message in msg:
        message_box.send_keys(message)
        time.sleep(2)
        #Finding send button
        button = browser.find_element_by_xpath('user input required')#//button[@class = "_1U1xa"]
        button.click()


browser.close()
browser.quit()
