from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Users\rohit\Desktop\Tor Browser\Browser\firefox.exe'

driver = webdriver.Firefox(firefox_profile=profile, executable_path= r'C:\Users\rohit\Desktop\Python_Projects\Crawler\geckodriver.exe', options=options)

driver.get("http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/")