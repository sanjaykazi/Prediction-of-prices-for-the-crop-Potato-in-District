"""
Title: Price Scrapping from Agmarknet
Created by: Sanjay Kazi
Date: 03/05/2021

"""

import requests
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
import time
PATH = "C:/Users/sanja/Desktop/web scrapping/agro/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get('https://agmarknet.gov.in/')
window_before = driver.window_handles[0]

# Prices/ Arrival
select_element1 = driver.find_element_by_id("ddlArrivalPrice")
select_object1 = Select(select_element1)
select_object1.select_by_visible_text('Price')
time.sleep(1)

# Commodity

select_element2 = driver.find_element_by_id("ddlCommodity")
select_object2 = Select(select_element2)
select_object2.select_by_visible_text('Potato')
time.sleep(1)

# State

select_element3 = driver.find_element_by_id("ddlState")
select_object3 = Select(select_element3)
select_object3.select_by_visible_text('Uttar Pradesh')
time.sleep(1)

# District

select_element4 = driver.find_element_by_id("ddlDistrict")
select_object4 = Select(select_element4)
select_object4.select_by_visible_text('Agra')
time.sleep(1)

# Market

select_element5 = driver.find_element_by_id("ddlMarket")
select_object5 = Select(select_element5)
select_object5.select_by_visible_text('--Select--')
time.sleep(1)

#Date variable initiation
input_date_from = driver.find_element_by_id("txtDate")
input_date_to = driver.find_element_by_id("txtDateTo")

# Date From
input_date_from.clear()
input_date_from.send_keys("01-Jan-2020")
time.sleep(1)

# Date To
input_date_to.clear()
input_date_to.send_keys("31-Dec-2020")
time.sleep(1)

# click Go button
driver.find_element_by_id("btnGo").click()
driver.forward()

time.sleep(20)
#download button
driver.find_element_by_id("cphBody_ButtonExcel").click()

print("Code executed succesfully!")
