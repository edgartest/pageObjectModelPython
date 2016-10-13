# Tests with the page object pattern.
import unittest
from selenium import webdriver
import basepage

class NavigationTests(unittest.TestCase):  
  def setUp(self):
    self.browser = webdriver.Firefox()
                          
  def tearDown(self):
    self.browser.close()
 
  def test_navigate_ticketsPage(self):
    home_page = basepage.HomePage(self.browser)
    home_page.navigate()
    print("Assertion that title is expected - Home Page")
    assert home_page.is_title_matches(), "Walt Disney World Title does not match!"
    tickets_page = home_page.navigateTicketsPage()
    print("Assertion that title is expected - Tickets Page")
    assert tickets_page.is_title_matches(), "Tickets"

  def test_selection_of_tickets(self):
    home_page = basepage.HomePage(self.browser)
    home_page.navigate()
    tickets_page = home_page.navigateTicketsPage()
    print("Selecting 1 Ticket 1 Adult Magic Kingdom")
    tickets_page = basepage.TicketsPage(self.browser)
    tickets_page.selectTickets(1)

if __name__ == '__main__':
    unittest.main()