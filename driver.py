# coding=utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

cartoon_name = '一拳超人'

driver = webdriver.Chrome("/mnt/d/Code/PycharmProjects/chromedriver.exe")
# driver = webdriver.PhantomJS()

driver.get("https://www.manhuadui.com/")

driver.find_element_by_id("keywords").send_keys(cartoon_name)
time.sleep(1)
driver.find_element_by_id("btnSearch").click()

time.sleep(1)
driver.find_element_by_xpath("//li[@class='list-comic']//a[text()='{}']".format(cartoon_name)).click()

# time.sleep(1)
# driver.find_element_by_xpath("//a[@class='beread_btn']").click()
time.sleep(3)
# lis = driver.find_elements_by_xpath("//ul[@id='chapter-list-1']/li/a")
driver.find_element_by_xpath("//ul[@id='chapter-list-1']/li[last()]/a").click()

# print("*******%d******" % len(lis))
driver.switch_to_window(driver.window_handles[2])
for i in range(100):
    time.sleep(5)
    driver.find_element_by_xpath("//span[@class='next']/a").click()

# driver.save_screenshot("./temp/manhuadui5.png")

driver.quit()
