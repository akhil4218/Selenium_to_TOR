import selenium
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.common.keys import Keys
                      
binary=FirefoxBinary("H:\\Tor_complete\\Tor Browser\\Browser\\firefox.exe")

profile = FirefoxProfile("H:\\Tor_complete\\Tor Browser\\Browser\\TorBrowser\\Data\\Browser\\profile.default")


driver=webdriver.Firefox(firefox_binary=binary,firefox_profile=profile)

driver.get("http://www.google.com")
time.sleep(3)
s=driver.find_element_by_xpath('//input[@id="lst-ib"]')
s.click()
s.clear()
s.send_keys("Sundar Pichai")
s.send_keys(Keys.RETURN)

time.sleep(3)
