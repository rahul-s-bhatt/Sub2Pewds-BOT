from time import sleep
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# This 3 lines gets the user-data for chrome login , so you can login in selenium webdriver chrome
options = Options()
options.add_argument("user-data-dir=~/.config/google-chrome")
browser = webdriver.Chrome('./chromedriver', chrome_options=options)

# Redirects you to Pewds channel
browser.get('https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw')
# Now get that subscribe button
sub2pewds = browser.find_element_by_id('subscribe-button')
# Click on it bruh smh
sub2pewds.click()

# Have paitence, not everyone has good internet :)
sleep(1)

# T-series channel here i come...
browser.get('https://www.youtube.com/user/tseries')

# Get the subscribed button, and click on it
unSubfromT = browser.find_element_by_id('subscribe-button')
unSubfromT.click()

# Click on the confirmation button
confirmButton = browser.find_element_by_id('confirm-button')
confirmButton.click()

sleep(5)
browser.close()
