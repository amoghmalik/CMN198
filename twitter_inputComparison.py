# Written by Joel Fischbein
#email account : cmn198twitterbot@gmail.com
#email password: sentiment


from selenium import webdriver
from time import sleep
import csv

#globals

searchterm = "happy"

driver = webdriver.Chrome('./chromedriver') # To be used for biasing Twitter account then scraping recommended users

#functions

#opens browser to twitter
def open_browser():
    driver.get('https://www.twitter.com/login')

#logs browser into research account
def login():
    email = "cmn198twitterbot@gmail.com"
    password = "sentiment"
    email_css = 'input.js-username-field.email-input.js-initial-focus'

    twitter_email = driver.find_element_by_css_selector(email_css).send_keys(email)
    twitter_passwd = driver.find_element_by_class_name('js-password-field').send_keys(password)
    twitter_submit = driver.find_element_by_css_selector('button.submit.btn.primary-btn').click()

def stall(seconds):
    sleep(seconds)

if __name__ == '__main__':
    open_browser()
    login()

    driver.close()