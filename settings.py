VERSION = "1.0"
DRIVER = ""
from os import environ 

from selenium import webdriver
#By default all driver binaries are saved to user.home/.wdm folder. 
#Override this setting to save binaries to project.root/.wdm.

environ['WDM_LOCAL'] = '1'


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())

