# coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome("/mnt/d/Code/PycharmProjects/chromedriver.exe")
#driver = webdriver.PhantomJS()

driver.get("https://www.manhuadui.com/")

time.sleep(3)
driver.save_screenshot("./temp/manhuadui2.png")

#time.sleep(3)
driver.quit()
