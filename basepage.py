from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BasePage(object):
	url = None

	def __init__(self, driver):
		self.driver = driver
		self.driver.implicitly_wait(5)
		self.timeout = 30

	def navigate(self):
		self.driver.get(self.url)

class HomePage(BasePage):
	url = "http://disneyworld.disney.go.com/"
	ticketsButton = (By.XPATH,'//*[@class="gnbCategory gnbParksAndTickets"]/a')

	def is_title_matches(self):
		return "Walt Disney World" in self.driver.title

	def navigateTicketsPage(self):
		webTicketsButton = self.driver.find_element(*HomePage.ticketsButton)
		webTicketsButton.click()
		return TicketsPage(self.driver)

class TicketsPage(BasePage):
	url = "http://disneyworld.disney.go.com/tickets"
	important_1_day_info = (By.ID, 'open-oneDayTickets-dialog')

	def is_title_matches(self):
		return "Tickets" in self.driver.title

	def selectTickets(self, daySelected):
		daysList = self.driver.find_elements_by_class_name('pepDayScroller_dayNum')
		daySelectedStr = str(daySelected)
		for day in daysList:
			dayDisplayed = day.text
			if(dayDisplayed == daySelectedStr):
				print("Found !!!")
				day.click


