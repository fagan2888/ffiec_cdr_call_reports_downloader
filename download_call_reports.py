import sys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

webLocation = "https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx"

try:
    driverLocation = sys.argv[1]
    browser = webdriver.Chrome(driverLocation)
except IndexError:
    browser = webdriver.Chrome()
finally:
    browser.get(webLocation)

# Step 1: Select one from Available Products
listBox1 = browser.find_element_by_id("ListBox1")
Select(listBox1).select_by_visible_text("Call Reports -- Single Period")

# Step 2: Select one of Available File Formats
browser.find_element_by_id("TSVRadioButton").click()

# Step 3: List all dates on dropdown menu from Reporting Period End Date
datesDropDownList = browser.find_element_by_id("DatesDropDownList")
select = Select(datesDropDownList)  # select is the drop-down menu
availableDates = [date.text for date in select.options]

# Step 4: Click Download button for each available date
for date in availableDates:
    datesDropDownList = browser.find_element_by_id("DatesDropDownList")
    Select(datesDropDownList).select_by_visible_text(date)
    browser.find_element_by_id("Download_0").click()
