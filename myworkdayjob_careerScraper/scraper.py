from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import re
import os
from operator import itemgetter 
import json
import time
import csv 
from fake_useragent import UserAgent
_url = "https://coke.wd1.myworkdayjobs.com/coca-cola-careers/jobs"
ua =UserAgent()
chrome_options = Options()
def get_results():

	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get(url=_url)
	wait = WebDriverWait(driver, 20)
	time.sleep(10)
	soup = BeautifulSoup(driver.page_source,'lxml')


	sections_ = soup.find('section',{"class":"css-8j5iuw"})
	total_pages = sections_.find('ul')["aria-label"]


	total_pages = total_pages.replace("Page 1 of ","")
	i = 2
	total_pages = int(total_pages)
	temp = 2

	while i <= total_pages:
		jobLocations = []
		jobType = []
		jobPostedDate = []
		jobReqId = []
		jobAddress = []
		job = sections_.find('li',{"class":"css-1q2dra3"})

		for job in sections_.find_all('li',{"class":"css-1q2dra3"}):

			job = job.find("h3")
			job = job.find("a",{"class":"css-u4dk0q"})["href"]
			linkToJob = "https://coke.wd1.myworkdayjobs.com" + job
			jobAddress.append(linkToJob)
			driver.get(url=linkToJob)
			wait = WebDriverWait(driver, 20)
			time.sleep(10)
			soup2 = BeautifulSoup(driver.page_source,'lxml')
			jobTitle = soup2.find("h2",{"class","css-7papts"}).get_text()
			jobDetails = soup2.find("div",{"class":"css-11p01j8"})
			jobDetails = jobDetails.find("div",{"class":"css-1pv4c4t"})

			for detail in jobDetails.find_all("div",{"class":"css-k008qs"}):

				temp = detail["data-automation-id"]
				if temp == "locations":
					jobLocations.append(detail.find("dd",{"class":"css-129m7dg"}).get_text())
				elif temp == "time":
					jobType.append(detail.find("dd",{"class":"css-129m7dg"}).get_text())
				elif temp == "postedOn":
					jobPostedDate.append(detail.find("dd",{"class":"css-129m7dg"}).get_text())
				elif temp == "requisitionId":
					jobReqId.append(detail.find("dd",{"class":"css-129m7dg"}).get_text())

			with open('cocaCola.csv', 'w') as f:
				writer = csv.writer(f)
				a_zip = zip(jobAddress , jobLocations, jobType,jobPostedDate, jobReqId)
				writer.writerow(a_zip)


			del jobLocations[:]
			del jobType[:]
			del jobPostedDate[:]
			del jobReqId[:]

	
		# driver.switch_to_window(main_window)
		wait = WebDriverWait(driver, 30)
		time.sleep(20)
		driver.find_element_by_xpath("//button[text()=" + str(i) + "]").click()
		wait = WebDriverWait(driver, 30)
		time.sleep(20)
		soup = BeautifulSoup(driver.page_source,'lxml')
		i = i+1




if __name__ == '__main__':
	results = get_results()
	# print(seller(results))
	# print '\n'
	# print(buyer(results))







