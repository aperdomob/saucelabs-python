from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import environ
from sauceclient import SauceClient

# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'name': "python-test",
    'platform': "Mac OS X 10.9",
    'browserName': "chrome"
}

sauce_username = environ['SAUCE_USERNAME']
sauce_token = environ['SAUCE_ACCESS_KEY']

server_url = 'http://{}:{}@ondemand.saucelabs.com:80/wd/hub'.format(sauce_username, sauce_token)
driver = webdriver.Remote(
  command_executor=server_url,
  desired_capabilities=desired_cap)
  
# This is your test logic. You can add multiple tests here.
driver.get("http://www.google.com")

if not "Google" in driver.title:
    raise Exception("Unable to load google page!")

elem = driver.find_element_by_name("q")
elem.send_keys("Sauce Labs")
elem.submit()
print driver.title
  
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()

sauce_client = SauceClient(sauce_username, sauce_token)
 
# this belongs in your test logic
sauce_client.jobs.update_job(driver.session_id, passed=True)
