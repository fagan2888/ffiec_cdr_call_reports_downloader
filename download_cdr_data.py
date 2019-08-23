from selenium import webdriver
from selenium.webdriver.support.ui import Select


driverLocation = "C:/Users/apsql/.chromedriver_win32/chromedriver.exe"
webLocation = "https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx"

browser = webdriver.Chrome(driverLocation)
browser.get(webLocation)

# select by id="ListBox1" -> click label="CallReports -- SingleReports"
listBox1 = browser.find_element_by_id("ListBox1")
Select(listBox1).select_by_visible_text("Call Reports -- Single Period")

# select by id="TSVRadioButton" -> click
browser.find_element_by_id("TSVRadioButton").click()

# list all available dates on dropdown menu
datesDropDownList = browser.find_element_by_id("DatesDropDownList")
select = Select(datesDropDownList)  # select is the drop-down menu
availableDates = [date.text for date in select.options]

for date in availableDates:
    datesDropDownList = browser.find_element_by_id("DatesDropDownList")
    Select(datesDropDownList).select_by_visible_text(date)
    browser.find_element_by_id("Download_0").click()
