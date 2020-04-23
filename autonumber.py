#!/usr/bin/python3
#--

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import random
import sys


class instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r'/usr/bin/geckodriver')
        
    #'//input[@name="username"]'   
    #'//input[@name="password"]'

    def login(self, hashtag):
        
        driver = self.driver
        driver.get ('https://www.instagram.com/?hl=pt-br')
        time.sleep(2)
        self.user_element = driver.find_element_by_xpath("//input[@name='username']")
        self.user_element.clear()
        self.user_element.send_keys(self.username)
        self.password_element = driver.find_element_by_xpath("//input[@name='password']")
        self.password_element.clear()
        self.password_element.send_keys(self.password)
        self.password_element.send_keys(Keys.RETURN)
        time.sleep(3) 
        driver.get ('https://www.instagram.com/explore/tags/{}/?hl=pt-br'.format(hashtag))
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)       
        #abrir fotos
        driver.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]//a//div[@class="eLAPa"]').click()
        time.sleep(3)
        
        
        i = 0
        while i <= 10:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            #curtirfotos
            driver.find_element_by_xpath('//div[@class="eo2As "]//section//span//button[@class="wpO6b "]').click()
            time.sleep(5)
            driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            time.sleep(10)
            i = i + 1 
            
        
        
        
        
        
        
mothBot = instabot('deathmoth123@gmail.com','98124812')
mothBot.login('memesBR')

